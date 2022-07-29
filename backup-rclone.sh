#!/bin/sh
/usr/local/bin/rclone -vv --log-file=/var/log/backup-rclone.log sync /mnt/dadoscoopaco/ encrypt:/

