import requests
import time
import netifaces as ni
import ipaddress
import os
import json
from pathlib import Path

conf = None

def get_curr_dir(fil):
    return os.path.abspath(os.path.dirname(os.path.relpath(fil)))

def check_connetion():
    while True:
        r = requests.get("https://www.google.com/")
        if r.status_code == 200:
            break
        time.sleep(3)

def get_host_ip(device):
    ip = ni.ifaddresses(device)[ni.AF_INET][0]['addr']
    return ip

def get_addresses(ip):
    ip_list = ip.split(".")
    ip = ip_list[0]+"."+ip_list[1]+"."+ip_list[2]+"."+"0"
    address = [str(x) for x in ipaddress.IPv4Network(f"{ip}/24")]
    return address

def get_interface():
    global conf
    if conf is None:
        curr_dir = Path(get_curr_dir(__file__))
        fil = str(curr_dir.joinpath("conf.json"))
        with open(fil) as f:
            conf = json.load(f)
    return conf["interface"]