#!/bin/bash
set -e

# --- 0. Set variables ---
REPO_URL="https://github.com/youruser/arclap-station.git"
INSTALL_DIR="$HOME/arclap"

# --- 1. Update system and install dependencies ---
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y git gphoto2 lftp cron

# --- 2. Clone repo ---
rm -rf "$INSTALL_DIR"
git clone "$REPO_URL" "$INSTALL_DIR"

# --- 3. Move to install folder ---
cd "$INSTALL_DIR"

# --- 4. Create folders ---
source arclap-config.properties
mkdir -p "$local_photos_folder"
mkdir -p "$logs"
chmod 775 "$local_photos_folder"

# --- 5. Make scripts executable ---
chmod +x arclap-capture.sh

# --- 6. Setup cron job ---
CRON_JOB="*/$capture_interval_minutes $capture_start_hour-$capture_end_hour * * $capture_days $INSTALL_DIR/arclap-capture.sh >> $INSTALL_DIR/logs/arclap.log 2>&1"
(crontab -l 2>/dev/null | grep -v arclap-capture.sh ; echo "$CRON_JOB") | crontab -

echo "Bootstrap finished! Arclap station is ready."
