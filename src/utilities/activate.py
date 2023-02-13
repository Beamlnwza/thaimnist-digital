import os
import subprocess

venv_path = os.path.join(os.getcwd(), '.venv', 'Scripts', 'activate')

subprocess.run(f"source {venv_path}", shell=True)

# Your script logic goes here

print("The virtual environment has been activated and your script is running.")