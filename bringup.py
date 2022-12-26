from utils import get_curr_dir, read_history
from pathlib import Path
import subprocess

def check_ping(ip):
    cmd = f"fping -c1 {ip}"
    p = subprocess.run(cmd, shell=True, capture_output=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return True if p.returncode == 0 else False

def bringup(ip_target):
    cmd = f"bash bringup_remote.bash {ip_target}"
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    curr_dir = Path(get_curr_dir(__file__))
    target_fil = "history.db"
    if not curr_dir.joinpath(target_fil).exists() or not check_ping(read_history()):
        print("Starting scanning")
        script_path = str(curr_dir.joinpath("find_ip.py"))
        exec(open(script_path).read())
    ip_target = read_history()
    print("Turtlebot ip:", ip_target)
    # bringup(ip_target)