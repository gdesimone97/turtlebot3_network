import socket
import requests

# requests.get("http://192.138.1.1", timeout=0.1)

TELEGRAM_SERVER = "server-peppodesmo.ddns.net"
# TELEGRAM_SERVER = "193.205.163.163"
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((TELEGRAM_SERVER, 9090))
data = "192.168.1.1"
clientSocket.send(data.encode())