from vars import rsync_windows, rclone_backup

# Lista de funcoes de backup
# Exemplo: lista_funcoes = [rsync_windows, rclone_backup]
lista_funcoes = [rsync_windows, rsync_windows]

#Config do rsync windows
rsync_password = "passswd"
rsync_user = "administrador"
rsync_windows_host = "192.168.0.1"
rsync_options = ""
rsync_origem = "/cygdrive/e/pasta/"
rsync_dest = "rsync://192.168.0.2:/Backup/pasta/"
rsync_log_file = "/var/log/backup-rsync.log"

#Config do rclone backup
rclone_binary = "/usr/local/bin/rclone"
rclone_config_file = "/mnt/dados/scripts/rclone.conf"
rclone_log_file = "/var/log/backup-rclone.log"
rclone_origem = "/mnt/dados/"
rclone_dest = "encrypt:/"


