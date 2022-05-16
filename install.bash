#!/bin/bash

sudo apt update
sudo apt-get install -y net-tools
sudo apt-get install -y python3-venv
python3 -m venv venv
source ./venv/bin/activate
pip install flask
pip install requests
pip install netifaces
sudo apt-get install -y ros-noetic-joy ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
  ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
  ros-noetic-rosserial-python ros-noetic-rosserial-client \
  ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
  ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
  ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
  ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers 
sudo apt install -y ros-noetic-dynamixel-sdk
sudo apt install -y ros-noetic-turtlebot3-msgs
sudo apt install -y ros-noetic-turtlebot3
cd $HOME
echo "export ROS_MASTER_URI=http://192.168.1.1:11311" >> .bashrc
echo "export ROS_HOSTNAME=192.168.1.1" >> .bashrc
echo "export TURTLEBOT3_MODEL=waffle_pi" >> .bashrc
