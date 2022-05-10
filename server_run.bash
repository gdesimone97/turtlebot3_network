#!/bin/bash

sleep 3
source $HOME/code/network/venv/bin/activate
python3 $HOME/code/network/server.py > /home/gdesimone/code/network/log.txt
