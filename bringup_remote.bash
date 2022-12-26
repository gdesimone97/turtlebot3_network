#!/bin/bash

sshpass -p turtlebot ssh -o StrictHostKeyChecking=no ubuntu@$1 /home/ubuntu/run/bringup_custom $2