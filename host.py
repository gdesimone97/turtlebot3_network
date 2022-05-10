import subprocess
import requests
from utils import check_connetion, get_host_ip
from pathlib import Path
import os

if __name__ == "__main__":
    check_connetion()
    ip = get_host_ip()
    exe_path = os.path.abspath(os.path.dirname(os.path.relpath(__file__)))
    exe_path = Path(exe_path).joinpath("modify.py")
    cmd = f"python3 {exe_path} {ip} {ip}"
    cmd = cmd.split(" ")
    r = subprocess.run(cmd)
    print("Return code:", r.returncode)

