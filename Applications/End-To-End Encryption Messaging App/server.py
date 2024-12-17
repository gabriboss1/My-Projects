import socket
from threading import Thread

def broadcast(message, sender_socket=None):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode('utf-8'))
            except:
                remove_client(client_socket)

def remove_client(client_socket):
    if client_socket in clients:
        username = usernames[client_socket]
        print(f"{username} has disconnected.")
        clients.remove(client_socket)
        del usernames[client_socket]
        client_socket.close()

def handle_client(client_socket):
    username = client_socket.recv(1024).decode()        
    usernames[client_socket] = username
    print(f"{username} has joined the chat.")
    
    for message in message_history:
        print(f"MESSAGE: {message}")
        message += "\n"
        client_socket.send(message.encode('utf-8'))

    while True:
        try:
            message = ""
            while True:
                part = client_socket.recv(1024).decode('utf-8')
                message += part
                if len(part) < 1024:
                    break

            if not message:
                break

            print(message)
            message_history.append(message)
            broadcast(message, sender_socket=client_socket)
        except Exception as e:
            print(f"Error handling client {username}: {e}")
            remove_client(client_socket)
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 2**16)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2**16)
    print("Server started and waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        clients.append(client_socket)
        Thread(target=handle_client, args=(client_socket,)).start()

clients = []
usernames = {}
message_history = []

start_server()
