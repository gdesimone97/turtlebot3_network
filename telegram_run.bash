#!/bin/bash

sleep 3
DIR=$HOME/turtlebot3_network
source $DIR/venv/bin/activate
python3 $DIR/telegram_bot.py > $DIR/log.txt
