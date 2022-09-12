import subprocess
import sys

lista_acl_obj = [
    'user:root',
    'owner@',
    'group@',
    'everyone@',
]

caminho = sys.argv[1]


for obj in lista_acl_obj:
    subprocess.call(f'{obj}:rwxpDdaARWcCo-:fd-----:allow {caminho}', shell=True)