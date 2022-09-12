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
    comando = f'setfacl -R -m {obj}:rwxpDdaARWcCo-:fd-----:allow {caminho}'
    print(comando)
    subprocess.call(comando, shell=True)