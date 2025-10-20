#!/bin/bash
set -e

# Load config
source config.properties

# Generate filename
FILENAME="$local_photos_folder/photo_$(date +%Y%m%d_%H%M%S).jpg"

# Capture photo using gphoto2
gphoto2 --set-config capturetarget=1 \
        --capture-image-and-download \
        --filename "$FILENAME" \
        --force-overwrite

# Upload to FTP
lftp -u "$ftp_user","$ftp_password" "$ftp_host" <<EOF
cd $ftp_folder
put "$FILENAME"
bye
EOF

# Optional: remove local file after upload
rm -f "$FILENAME"
