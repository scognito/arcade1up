import RPi.GPIO as GPIO
from time import sleep
import subprocess
import re

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

volume_delta = 5
sleep_val = 0.3

def get_current_volume():
    try:
        # Run pactl command to list sinks
        result = subprocess.run(["pactl", "list", "sinks"], capture_output=True, text=True, check=True)
        output = result.stdout

        # Find the active sink (state RUNNING)
        active_sink = None
        for sink in output.split("Sink #"):
            if "State: RUNNING" in sink:
                active_sink = sink
                break

        if not active_sink:
            print("No active sink found.")
            return 0

        # Extract the volume percentage
        match = re.search(r"Volume: .*?(\d+)%", active_sink)
        if match:
            return int(match.group(1))
        else:
            print("Volume not found in active sink.")
            return 0
    except subprocess.CalledProcessError as e:
        print(f"Error running pactl: {e}")
        return 0

def set_volume(volume):
    # Ensure volume is within bounds
    volume = max(0, min(100, volume))
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{volume}%"])
    print(f"Volume set to {volume}%")

# Initialize volume to the current value
volume_state = get_current_volume()
print(f"Initial volume: {volume_state}%")

while True:

    volume_state = get_current_volume()
    #print(f"Initial volume: {volume_state}%")

    button_state1 = GPIO.input(12)
    button_state2 = GPIO.input(16)

    if button_state1 and button_state2 and volume_state < 100:
        print("Switch was set to HIGHER")
        volume_state += volume_delta
        set_volume(volume_state)
        sleep(sleep_val)

    if not button_state1 and not button_state2 and volume_state > 0:
        print("Switch was set to LOWER")
        volume_state -= volume_delta
        set_volume(volume_state)
        sleep(sleep_val)
