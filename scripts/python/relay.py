import RPi.GPIO as GPIO

print("Starting " + __file__)

pinRelay = 22
#pinRelay = 36

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinRelay, GPIO.OUT)
GPIO.output(pinRelay, GPIO.HIGH)

print("Finishing " + __file__)
