import socket 

def client(msg):
    message = str(msg)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 10000))
    sock.send(message.encode())
    data = sock.recv(1024).decode()
    print(data)
    sock.close()

if __name__ == '__main__':
    try:
        client1 = client("Bonjour1")
        client1 = client("arret")
    except ConnectionRefusedError:
        print("Le serveur n'est pas lancé")
    except ConnectionResetError:
        print("Connection fermée")
    
    # client2 = client("Bonjour2")
    # client2 = client("arret")