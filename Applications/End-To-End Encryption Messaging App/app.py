import socket
from threading import Thread
from datetime import datetime


server_ip = "1.2.3.4" # Enter server IP here.
server_port = 12345


def generate_rsa_keys():
    p, q = 1000000000000000035000061, 1015402101225201202154011
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi)
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

def rsa_encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def rsa_decrypt(encrypted_message, private_key):
    n, d = private_key
    return ''.join(chr(pow(int(char), d, n)) for char in encrypted_message)

def receive_messages(client_socket, private_key):
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

            split_message = message.split(": ", 1)
            timestamp_and_username = split_message[0]
            encrypted_message_str = split_message[1]

            encrypted_message_str = encrypted_message_str.replace('[', '')
            encrypted_message_str = encrypted_message_str.replace(']', '')

            while True:
                # print(encrypted_message_str)
                if "-" in encrypted_message_str:
                    i = encrypted_message_str.index("-")
                    end_of_timestamp = encrypted_message_str.find(' ', 24) + 1
                    encrypted_message_str = encrypted_message_str[end_of_timestamp:]
                else:
                    break

            encrypted_message = [int(num.strip()) for num in encrypted_message_str.split(',') if num.strip().isdigit()]

            decrypted_message = rsa_decrypt(encrypted_message, private_key)
            print(f"{timestamp_and_username}: {decrypted_message}")
        except Exception as e:
            print("Error receiving message:", e)
            break

def start_client():
    client_socket = socket.socket()
    client_socket.connect((server_ip, server_port))

    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))

    # Generate RSA keys
    public_key, private_key = generate_rsa_keys()

    Thread(target=receive_messages, args=(client_socket, private_key), daemon=True).start()

    while True:
        try:
            message = input()
            if message.lower() == 'bye':
                break

            encrypted_message = rsa_encrypt(message, public_key)

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            formatted_message = f"[{timestamp}] {username}: {encrypted_message}"

            client_socket.send(formatted_message.encode('utf-8'))

        except Exception as e:
            print("Error sending message:", e)
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()
