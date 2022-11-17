import socket 

server_socket = socket.socket()
server_socket.bind(('localhost', 10000))
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
conn.send(data.encode())
conn.close()
