#!/bin/bash
set -e

# --- 1. Update system and install dependencies ---
echo "Updating system and installing dependencies..."
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y gphoto2 lftp cron

# --- 2. Create local folders ---
echo "Creating local folders..."
source config.properties
mkdir -p "$local_photos_folder"
mkdir -p logs
chmod 775 "$local_photos_folder"

# --- 3. Make capture script executable ---
chmod +x arclap-capture.sh

# --- 4. Setup cron job ---
echo "Setting up cron job..."
CRON_JOB="* * * * * $PWD/arclap-capture.sh >> $PWD/logs/arclap.log 2>&1"
# replace with interval from config
CRON_INTERVAL="*/$capture_interval_minutes $capture_start_hour-$capture_end_hour * * $capture_days"
(crontab -l 2>/dev/null | grep -v arclap-capture.sh ; echo "$CRON_INTERVAL $PWD/arclap-capture.sh >> $PWD/logs/arclap.log 2>&1") | crontab -

echo "Bootstrap finished! Arclap station is ready."
