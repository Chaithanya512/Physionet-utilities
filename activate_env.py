import subprocess
import os

def activate_env():
    venv_path = '/home/giladgressel/eusml/bin/activate'
    subprocess.run(f"source {venv_path}", shell=True, executable="/bin/bash")
    subprocess.run(['python3', 'run_train.py'])


if __name__ == '__main__':
    activate_env()