#!/home/gdesimone/code/bash_runtime/venv/bin/python3
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("master_ip", type=str)
    parser.add_argument("hostname", type=str)
    args = parser.parse_args()

    home = os.environ["HOME"]
    path = fr"{home}/.bashrc"
    regex = r".\+[0-9]\+.[0-9]\+.[0-9]\+.[0-9]\+"
    old = fr'export ROS_MASTER_URI={regex}'
    new = fr'export ROS_MASTER_URI=http://{args.master_ip}:11311'
    cmd = fr"sed -i 's|{old}|{new}|g' {path}"
    os.system(cmd)

    old = fr'export ROS_HOSTNAME=[0-9]\+.[0-9]\+.[0-9]\+.[0-9]\+'
    new = fr'export ROS_HOSTNAME={args.hostname}'
    cmd = fr"sed -i 's|{old}|{new}|g' {path}"
    os.system(cmd)