import subprocess
import os
from pathlib import Path
import datetime

rclone_binary = "/usr/local/bin/rclone"
rclone_config_file = "/mnt/dados/scripts/rclone.conf"
rclone_log_file = "/var/log/backup-rclone.log"
rclone_origem = "/mnt/dados/"
rclone_dest = "encrypt:/"

rsync_password = "passswd"
rsync_user = "administrador"
rsync_windows_host = "192.168.0.1"
rsync_options = "--exclude 'Banco'"
rsync_origem = "/cygdrive/e/pasta/"
rsync_dest = "rsync://192.168.0.2:/Backup/pasta/"
rsync_log_file = "/var/log/backup-rsync.log"


status_file = "/var/log/backup_status"


def compress_file(file):
    subprocess.call(f"gzip {file}", shell=True)


def rename_file(file1, file2):
    os.rename(file1, file2)


def rotate_file(filepadrao):
    file_path = Path(filepadrao)
    file_list = file_path.parent.rglob(file_path.name + "*")
    for file_obj in file_list:
        file = str(file_obj)
        list_name_file = file.strip(".")
        if file == filepadrao:
            compress_file(file)
        elif file == filepadrao + ".gz":
            os.rename(file, file + ".1")
        elif list_name_file[2] in [str(i) for i in range(2, 8)]:
            os.rename(file, list_name_file[0] + "gz" + str(int(list_name_file[2]) + 1))
        else:
            os.remove(file)


def run_backup_rclone():
    exec_status = subprocess.call(
        f"{rclone_binary} -v --config {rclone_config_file} --log-file {rclone_log_file} sync {rclone_origem} encrypt:/",
        shell=True,
    )
    return exec_status


def run_backup_rsync():
    exec_status = subprocess.call(
        f"sshpass -p {rsync_password} ssh {rsync_user}@{rsync_windows_host} 'rsync -rtv --delete {rsync_options} {rsync_origem} {rsync_dest}' > {rsync_log_file} 2>&1",
        shell=True
    )
    return exec_status


def run_backup():
    rsync_status = run_backup_rsync()
    rclone_status = run_backup_rclone()
    status = rclone_status + rsync_status
    with open(status_file, 'w') as f:
        f.write(str(status))
    if datetime.datetime.today().day in [7, 14, 28]:
        rotate_file(rclone_log_file)
        rotate_file(rsync_log_file)


run_backup()
