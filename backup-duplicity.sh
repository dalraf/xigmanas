#!/bin/bash
export PASSPHRASE=passwd
duplicity -v 3 /mnt/dadoscoopaco/ rsync://10.139.0.121::Backup/coopaco/

