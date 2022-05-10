#!/bin/bash

sleep 3
source $HOME/turtlebot3_network/venv/bin/activate
python3 $HOME/turtlebot3_network/host.py > $HOME/turtlebot3_network/log_host.txt
