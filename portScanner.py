import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "10.0.0.92"
port = 80

def portScanner(port):
    if s.connect_ex(host, port):
        print("The port is closed")
    else:
        print("The port is open")
