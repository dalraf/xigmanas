iimport subprocess
import sys

def set_permissions(directory):
    subprocess.run(["setfacl", "-R", "-b", directory])
    subprocess.run(["chown", "-R", "root", directory])
    subprocess.run(["chgrp", "-R", "wheel", directory])
    subprocess.run(["setfacl", "-R", "-m", "group@:full_set:fd:allow", directory])
    subprocess.run(["setfacl", "-R", "-m", "owner@:full_set:fd:allow", directory])
    subprocess.run(["setfacl", "-R", "-m", "everyone@:full_set:fd:allow", directory])
    subprocess.run(["setfacl", "-R", "-m", "group:usuários_do_domínio:rwxpDdaARWcCos:fd-----:allow", directory])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    set_permissions(directory)
