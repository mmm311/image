import socket
import sys
HOST = "127.0.0.1"
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    conn, addr = s.accept()
    while True:
        print("Connected by", addr)
        data = conn.recv(1024)
        print(data)
        conn.sendall(data)


