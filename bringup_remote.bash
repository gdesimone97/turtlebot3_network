#!/bin/bash

sshpass -p turtlebot ssh -o StrictHostKeyChecking=no ubuntu@$1 /bin/bash
sshpass -p turtlebot ssh -o StrictHostKeyChecking=no ubuntu@$1 ps aux | grep turtlebot3_robot.launch | awk "{print $1}"