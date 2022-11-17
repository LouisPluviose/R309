import socket

def serveur():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 10000))
    server_socket.listen(2)
    print("Serveur en attente de connexion")
    conn, address = server_socket.accept()
    data = conn.recv(1024).decode()
    if data == "arret":
        data = "Serveur arrete"
        conn.send(data.encode())
        conn.close()
        server_socket.close()
    elif data == "bye":
        data = "Au revoir"
        print("Fermeture de la connexion")
        conn.send(data.encode())
        conn.close()
    else:
        conn.send(data.encode())
        print("Réception d'un message")
        print(data)


if __name__ == '__main__':
    serveur()
