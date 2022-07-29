#!/bin/sh
sshpass -p passwd ssh administrador@192.168.2.10 'rsync -rtv --delete --exclude 'Banco' /cygdrive/e/Syscoop3/  rsync://192.168.2.248:/Backup/syscoop3/'
