import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 10000))
client_socket.send("message".encode())
data = client_socket.recv(1024).decode()
client_socket.close()