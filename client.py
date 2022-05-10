import socket
import requests

# requests.get("http://192.138.1.1", timeout=0.1)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("127.0.0.1",9090))
data = "192.168.1.1"
clientSocket.send(data.encode())