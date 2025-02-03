import os
import subprocess
import sys

def install_requirements():
    python_executable = find_venv() or sys.executable
    subprocess.run([python_executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

def find_venv():
    possible_venvs = ['.venv', 'venv', 'env', 'ENV']
    for venv in possible_venvs:
        venv_path = os.path.join(os.getcwd(), venv, 'Scripts', 'python')
        if os.path.exists(venv_path):
            return venv_path
    return None

def run_scripts():

    #install_requirements()

    scripts = [
        "allpass-waffle\\bot.py",
    ]
    
    python_executable = find_venv() or sys.executable
    
    for script in scripts:
        subprocess.run([python_executable, script], check=True)

if __name__ == "__main__":
    run_scripts()