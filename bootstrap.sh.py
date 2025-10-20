#!/bin/bash
set -e

echo "=== Arclap Station Setup Starting ==="

# --- 1. Update system and install dependencies ---
echo "Updating system and installing dependencies..."
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y gphoto2 lftp cron

# --- 2. Load configuration ---
source arclap-config.properties

# --- 3. Create local folders ---
echo "Creating local folders..."
mkdir -p "$arclap_local_photos"
mkdir -p "$arclap_log_folder"
chmod 775 "$arclap_local_photos"

# --- 4. Make capture script executable ---
chmod +x arclap-capture.sh

# --- 5. Setup cron job ---
echo "Setting up cron job..."
CRON_ENTRY="*/$arclap_capture_interval $arclap_capture_start_hour-$arclap_capture_end_hour * * $arclap_capture_days $PWD/arclap-capture.sh >> $PWD/$arclap_log_folder/arclap.log 2>&1"
(crontab -l 2>/dev/null | grep -v arclap-capture.sh ; echo "$CRON_ENTRY") | crontab -

echo "=== Arclap Station Setup Complete! ==="
