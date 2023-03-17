if [ "$#" -ne 1 ]; then
	echo "Illegal number of parameters"
	exit
fi
sudo apt update
sudo apt install -y sshpass fping python3-pip
python3 -m pip install -r requirements.txt
sudo chmod +x get_ip_wlan
sudo cp get_ip_wlan /usr/local/bin
export INTERFACE=$1
USR=$(whoami)
source /home/$USR/.bashrc
echo "export TURTLEBOT3_MODEL=waffle_pi" >> /home/$USR/.bashrc
echo "export INTERFACE=$INTERFACE" >> /home/$USR/.bashrc
echo "IP=$(get_ip_wlan)" >> /home/$USR/.bashrc
echo "export ROS_MASTER_URI=http://\$IP:11311/" >> /home/$USR/.bashrc
echo "export ROS_HOSTNAME=\$IP" >> /home/$USR/.bashrc
