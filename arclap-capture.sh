#!/bin/bash
set -e

source arclap-config.properties

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOCAL_FILE="$arclap_local_photos/photo_$TIMESTAMP.jpg"

# Capture image
gphoto2 --set-config capturetarget=1 \
        --capture-image-and-download \
        --filename "$LOCAL_FILE" \
        --force-overwrite

# Upload to FTP
lftp -u "$arclap_ftp_user","$arclap_ftp_password" "$arclap_ftp_host" <<EOF
cd $arclap_ftp_folder
put "$LOCAL_FILE"
bye
EOF

# Remove local file
rm -f "$LOCAL_FILE"
