import subprocess

def run_scripts():
    scripts = [
        "allpass-waffle/bot.py",
    ]
    
    python_executable = "python"
    
    for script in scripts:
        subprocess.run([python_executable, script], check=True)

if __name__ == "__main__":
    run_scripts()