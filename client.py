import socket
s = socket.socket()

HOST = "127.0.0.1"
PORT = 51675

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
 #   s.sendall(b"Hello world")
    while True:
       message = input()
       s.sendall(bytes(message, encoding="utf-8"))
       data = s.recv(1024)
       print("Received", repr(data))
