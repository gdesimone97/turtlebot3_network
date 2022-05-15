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

def get_host_submask(device):
    netmask = ni.ifaddresses(device)[ni.AF_INET][0]['netmask']
    return netmask

def get_host_broadcast(device):
    broadcast_ip = ni.ifaddresses(device)[ni.AF_INET][0]['broadcast']
    return broadcast_ip

def address2bit_number(address):
    address = address.split(".")
    adr_out = []
    for adr in address:
        adr_out.append(bin(adr).count("1"))
    count = sum(adr_out)
    return count

def get_addresses(ip):
    ip_list = ip.split(".")
    submask = get_host_submask(get_interface()).split(".")
    data = zip(ip_list, submask)
    ip_out_list = []
    for ip, mask in data:
        ip_out_list.append((ip & mask))
    ip_out = ip_out_list[0] + "." + ip_out_list[1] + "." + ip_out_list[2] + "." + ip_out_list[3]
    bit_number = address2bit_number(submask)
    address = [str(x) for x in ipaddress.IPv4Network(f"{ip_out}/{bit_number}")]
    return address

def get_interface():
    global conf
    if conf is None:
        curr_dir = Path(get_curr_dir(__file__))
        fil = str(curr_dir.joinpath("conf.json"))
        with open(fil) as f:
            conf = json.load(f)
    return conf["interface"]