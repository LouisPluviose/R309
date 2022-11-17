import socket
import threading
import time

def client():
    client_socket = socket.socket()
    client_socket.connect(('localhost', 10000))
    client_socket.send("message".encode())
    data = client_socket.recv(1024).decode()
    client_socket.close()

def server():
    server_socket = socket.socket()
    server_socket.bind(('localhost', 10000))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    data = conn.recv(1024).decode()
    conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    t1 = threading.Thread(target=server)
    t2 = threading.Thread(target=client)

    start = time.perf_counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.perf_counter()

    print(f"Took {round(end - start, 2)} seconds")