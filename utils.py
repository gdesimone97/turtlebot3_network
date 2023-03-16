import netifaces as ni
import os
import json
from pathlib import Path
import subprocess
import re

conf = None

def get_conf():
    global conf
    if conf is None:
        curr_dir = Path(get_curr_dir(__file__))
        fil = str(curr_dir.joinpath("conf.json"))
        with open(fil) as f:
            conf = json.load(f)
    return conf

def get_curr_dir(fil):
    return os.path.abspath(os.path.dirname(os.path.relpath(fil)))

def get_host_ip(interface):
    ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
    return ip

def get_host_submask(interface):
    netmask = ni.ifaddresses(interface)[ni.AF_INET][0]['netmask']
    netmask_int = str2list(netmask)
    netmask_length = get_netmasklenght(netmask_int)
    return netmask, netmask_length

def get_subnet(ip: str, netmask: str):
    ip_list = str2list(ip)
    netmask_list = str2list(netmask)
    subnet = []
    for ip, netmask in zip(ip_list, netmask_list):
        subnet.append(ip & netmask)
    return subnet

def get_netmasklenght(netmask: list) -> int:
    lenght = 0
    for n in netmask:
        n_bin = bin(n)
        lenght += n_bin.count("1")
    return lenght

def get_interface():
    # return get_conf()["interface"]
    try:
        return os.environ["INTERFACE"]
    except KeyError:
        raise Exception("You need to specify the INTERFACE variable into .bashrc file")

def list2str(data_list: list):
    str_list = ""
    for data in data_list:
        str_list += str(data) + "."
    return str_list[:-1]

def str2list(data_str: str):
    data_str_list = data_str.split(".")
    return list(map(lambda x: int(x), data_str_list))

def ping(subnet, netmask_length):
    subnet = list2str(subnet)
    cmd = f"fping -r 1 -g {subnet}/{netmask_length}"
    p = subprocess.run(cmd, check=False, capture_output=True, shell=True, text=True)
    return p.stdout

def get_ip_lives(ping_text: str):
    pattern = re.compile("\d+\.\d+\.\d+\.\d+")
    rows = ping_text.split("\n")
    ip_lives = []
    for row in rows:
        if "alive" in row:
            match = pattern.findall(row)[0]
            ip_lives.append(match)
    print("IP lives:", ip_lives)
    return ip_lives

def get_mac_list(ip_list: list):
    mac_list = []
    pattern = re.compile("\w+:\w+:\w+:\w+:\w+:\w+")
    cmd_raw = "arp -a {}"
    for ip in ip_list:
        cmd = cmd_raw.format(ip)
        p = subprocess.run(cmd, shell=True, capture_output=True, check=False, text=True)
        text = p.stdout
        try:
            mac = pattern.findall(text)[0]
        except IndexError:
            mac = None
        mac_list.append(mac)
    return mac_list

def write_history(ip_target):
    curr_dir = Path(get_curr_dir(__file__))
    target_fil = curr_dir.joinpath("history.db")
    with open(str(target_fil), "w") as fil:
        fil.write(ip_target)

def read_history():
    curr_dir = Path(get_curr_dir(__file__))
    target_fil = curr_dir.joinpath("history.db")
    with open(str(target_fil)) as fil:
        ip_target = fil.read()
        return ip_target

def check_mac(ip_mac_list: zip):
    ip_mac_list = list(ip_mac_list)
    print("IP MAC pairs:")
    print(ip_mac_list)
    mac_target = get_conf()["target_mac"]
    for ip, mac in ip_mac_list:
        if mac == mac_target:
            return ip
    raise Exception("Device not found")