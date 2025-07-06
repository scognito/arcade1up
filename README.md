# Arcade1Up Raspberry Pi GPIO Scripts

This repository contains the Python scripts and corresponding service files I used to integrate the original Arcade1Up **power** and **volume** buttons, as well as a **relay switch**, with a Raspberry Pi running Batocera.

## Demo video
Click on a thumbnail to watch the video

[![Watch the video](https://img.youtube.com/vi/gJHIdN8BHyQ/hqdefault.jpg)](https://youtube.com/shorts/gJHIdN8BHyQ?si=i6ses3GUSsEiI_OE)

[![Watch the video](https://img.youtube.com/vi/UPXLANCFOGA/hqdefault.jpg)](https://youtube.com/shorts/UPXLANCFOGA)

## Complete step by step tutorial
Read the full tutorial on my blog: [Link](https://scognito.wordpress.com/2025/07/06/step-by-step-mod-of-arcade1up-cabinet-with-a-raspberry-pi/)

## Features

- Safe shutdown via the original power switch
- Volume control using the original rocker button
- Automatic relay control to power external devices (e.g. marquee light and audio amplifier) on Raspberry Pi boot/shutdown

## File Structure

```
/userdata/system/
├── scripts/
│   └── python/
│       ├── power.py
│       ├── volume.py
│       └── relay.py
└── services/
    ├── rpi_power
    ├── rpi_volume
    └── rpi_relay
```

## Installation

1. Copy the `python` scripts to:
   ```
   /userdata/system/scripts/python/
   ```

2. Copy the service files to:
   ```
   /userdata/system/services/
   ```

3. Make sure all Python scripts are executable:
   ```bash
   chmod +x *.py
   ```

4. Reboot Batocera.

## Requirements

- Raspberry Pi (tested on Pi 4)
- Batocera
- GPIO access enabled

## License

MIT
