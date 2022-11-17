import socket
import multiprocessing

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


def client(msg):
    message = str(msg)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 10000))
    sock.send(message.encode())
    data = sock.recv(1024).decode()
    print(data)
    sock.close()

if __name__ == '__main__':
    thread_serveur = multiprocessing.Process(target=serveur)
    thread_serveur.start()

    thread_client = multiprocessing.Process(target=client, args=("Bonjour1",))
    thread_client.start()