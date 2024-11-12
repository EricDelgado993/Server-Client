import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive_messages():
    """ Function to receive messages from the server """
    while True:
        try:
            message = client.recv(2048).decode(FORMAT)
            print(f"Server: {message}")
        except:
            print("Disconnected from server.")
            break

def send(msg):
    """ Function to send messages to the server """
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

# Start a thread to receive messages from the server
thread = threading.Thread(target=receive_messages)
thread.start()

# Main loop to send messages
while True:
    msg = input("Enter a message (or '!list' to view connected clients): ")
    if msg == DISCONNECT_MESSAGE:
        send(DISCONNECT_MESSAGE)
        break
    elif msg == "!list":
        send("REQUEST_CLIENT_LIST")
    else:
        send(msg)

        # If user wants to send a message to another client, get client ID and message
        target_client_id = input("Enter target client ID (or press Enter to skip): ")
        if target_client_id:
            send(f"TO_CLIENT:{target_client_id}:{msg}")

client.close()