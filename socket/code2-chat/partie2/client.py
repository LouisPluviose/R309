import socket 
import multiprocessing
import time

def client(msg):
    message = str(msg)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 10000))
    sock.send(message.encode())
    data = sock.recv(1024).decode()
    print(data)
    sock.settimeout(5)


if __name__ == '__main__':
    try:
        thread_client = multiprocessing.Process(target=client, args=("Bonjour1",))
        thread_client.start()
    except ConnectionRefusedError:
        print("Le serveur n'est pas lancé")
    except ConnectionResetError:
        print("Connection fermée")
    except socket.timeout:
        print("Délai dépassé")
    
    # client2 = client("Bonjour2")
    # client2 = client("arret")