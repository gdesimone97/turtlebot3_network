# turtlebot

## Installation steps
1. Clone this repository
2. Locate in the repository folder. Ex. ```cd turtlebot3_network```
3. RUN ```ifconfig``` and copy your wlan interface
3. RUN ```bash install.bash <WLAN_INTERFACE>``` 
   - Note: The <WLAN_INTERFACE> is the one that you got with 3
   - Ex. ```bash install.bash wlp0s20f3```
4. RUN ```cd && source .bashrc```

## How to use
1. RUN ```python3 bringup.py```