#!/bin/bash

sleep 3
source $HOME/turtlebot3_network/venv/bin/activate
python3 $HOME/turtlebot3_network/host.py > /home/gdesimone/code/turtlebot/log_host.txt
