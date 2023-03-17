#!/usr/bin/python3

from utils import get_curr_dir, read_history, get_host_ip, get_interface
from pathlib import Path
import subprocess
import signal

def kill(*args):
    cmd_kill = '"ps aux | grep turtlebot3_robot.launch | pkill launch"'
    run_command(cmd_kill, ip_target, shell=False)

def check_ping(ip):
    cmd = f"fping -c1 {ip}"
    p = subprocess.run(cmd, shell=True, capture_output=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return True if p.returncode == 0 else False

def run_command(cmd, ip_turtle, background=False, shell=True):
    cmd_ssh = f"sshpass -p turtlebot ssh -o StrictHostKeyChecking=no ubuntu@{ip_turtle}"
    if shell:
        cmd_ssh += f" /bin/bash {cmd}"
    else:
        cmd_ssh += f" {cmd} "
    if background:
        p = subprocess.Popen(cmd_ssh, shell=True, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        p.communicate(cmd)
    else:
        p = subprocess.run(cmd_ssh, shell=True, stderr=subprocess.STDOUT)
    return p

def bringup(ip_target, ip_host):
    cmd = f"run/bringup_custom {ip_host}"
    cmd_kill = '"ps aux | grep turtlebot3_robot.launch | pkill launch"'
    run_command(cmd_kill, ip_target, shell=False)
    try:
        run_command(cmd, ip_target)
    except KeyboardInterrupt:
        pass
    run_command(cmd_kill, ip_target, shell=False)


if __name__ == "__main__":
    curr_dir = Path(get_curr_dir(__file__))
    target_fil = "history.db"
    if not curr_dir.joinpath(target_fil).exists() or not check_ping(read_history()):
        print("Starting scanning")
        script_path = str(curr_dir.joinpath("find_ip.py"))
        exec(open(script_path).read())
    ip_target = read_history()
    ip_host = get_host_ip(get_interface())
    print("Turtlebot ip:", ip_target )
    print("PC ip:", ip_host)
    signal.signal(signal.SIGINT, kill)
    bringup(ip_target, ip_host)