#!/bin/bash

sleep 3
source $HOME/turtlebot3_network/venv/bin/activate
python3 $HOME/turtlebot3_network/server.py > /home/gdesimone/code/network/log.txt
