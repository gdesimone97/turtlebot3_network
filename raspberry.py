import subprocess
import time
import requests
from utils import check_connetion, get_host_ip, get_addresses
from pathlib import Path
import os
import socket

def get_master_ip(adresses: list, client_ip):
    LIMIT = 3
    payload = {"client_ip": client_ip}
    count = 0
    while True:
        for ip in adresses:
            if ip.split(".")[-1] == "0":
                continue
            try:
                print(f"\r{ip}", end="")
                r = requests.get(f"http://{ip}:5000/ip", timeout=0.12, params=payload)
                ip = r.text
                return ip
            except requests.exceptions.ConnectTimeout:
                pass
        count += 1
        if count >= LIMIT:
            print("Not connected")
            print("Return code: -1")
        time.sleep(3)

def send_telegram(telegram_socket_ip, rasp_ip):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((telegram_socket_ip, 9090))
    data = rasp_ip
    print("\nSending", rasp_ip, "to", telegram_socket_ip)
    clientSocket.send(data.encode())

if __name__ == "__main__":
    # check_connetion()
    print("Configuration start")
    ip = get_host_ip("wlan0")
    addresses = get_addresses(ip)
    master_ip = get_master_ip(addresses, ip)
    send_telegram(master_ip, ip)
    exe_path = os.path.abspath(os.path.dirname(os.path.relpath(__file__)))
    exe_path = Path(exe_path).joinpath("modify.py")
    cmd = f"python3 {exe_path} {master_ip} {ip}"
    cmd = cmd.split(" ")
    r = subprocess.run(cmd)
    print("Return code:", r.returncode)