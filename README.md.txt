Purpose: Instructions for technicians.

# Arclap Station Setup

## One-Time Setup
1. Flash Raspberry Pi OS.
2. SSH into Pi:


ssh pi@<pi-ip>

3. Run bootstrap script:


curl -sSL <cloud-url>/arclap-station/bootstrap.sh | bash


## Config File
- `config.properties` contains FTP, folder paths, and schedule.
- Edit this file to change settings.

## Logs
- Logs are stored in `logs/arclap.log`.

## Capture Script
- `arclap-capture.sh` handles image capture and FTP upload.
- Runs automatically via cron based on `config.properties`.