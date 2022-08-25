#!/bin/sh
/usr/local/bin/rclone -v --config /mnt/dados/scripts/rclone.conf --syslog sync /mnt/dados/ encrypt:/

