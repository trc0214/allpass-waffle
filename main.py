import subprocess
import sys

def run_scripts():
    scripts = [
        "allpass-waffle/bot.py",
    ]

    # Use the current Python interpreter to avoid relying on an external "python" binary.
    python_executable = sys.executable

    for script in scripts:
        try:
            subprocess.run([python_executable, script], check=True)
        except FileNotFoundError as e:
            print(f"Executable not found: {python_executable}")
            raise
        except subprocess.CalledProcessError as e:
            print(f"Script {script} exited with return code {e.returncode}")
            raise

if __name__ == "__main__":
    run_scripts()