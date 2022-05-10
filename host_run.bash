#!/bin/bash

sleep 3
source $HOME/code/turtlebot/venv/bin/activate
python3 /home/gdesimone/code/turtlebot/host.py > /home/gdesimone/code/turtlebot/log_host.txt
