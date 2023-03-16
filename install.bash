
sudo apt update
sudo apt install -y sshpass fping
python3 -m pip install -r requirements.txt
sudo chmod +x get_ip_wlan
sudo cp get_ip_wlan /usr/local/bin
INTERFACE=$1
USR=$(whoami)
echo "export INTERFACE=$INTERFACE" >> /home/$USR/.bashrc
