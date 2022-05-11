#!/bin/bash

sudo apt update
sudo apt-get install -y net-tools
sudo apt-get install -y python3-venv
python3 -m venv venv
source ./venv/bin/activate
pip install flask
pip install requests
pip install netifaces
