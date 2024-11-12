import socket
import threading

HEADER = 64                                             # The length of the message to the server (64 bytes)
PORT = 5050                                             # Unused port for program
DISCONNECT_MESSAGE = "!DISCONNECT"                      # Tells the server that the client is disconnecting
SERVER = socket.gethostbyname(socket.gethostname())     # Gets the IPv4 address of the device
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)

# Tells socket what type of IP address to accept
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket into the address
server.bind(ADDR)

clients = {}
client_id_counter = 0
lock = threading.Lock()

def broadcast(message):

    # Sends a message to all clients
    for client in clients.values():
        client["conn"].send(message.encode(FORMAT))

def handle_client(conn, addr):

    # Handles client connections
    global client_id_counter
    client_id = None

    with lock:
        client_id_counter += 1
        client_id = client_id_counter
        clients[client_id] = {"conn": conn, "addr": addr}
    
    print(f"[NEW CONNECTION] {addr} connected with client ID {client_id}.")

    connected = True
    while connected:

        # Gets message and decondes into byte format
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            # Makes sure that the client is disconnected from the server
            if msg == DISCONNECT_MESSAGE:
                connected = False
            elif msg == "REQUEST_CLIENT_LIST":
                client_list = f"Connected clients: {', '.join(map(str, clients.keys()))}"
                conn.send(client_list.encode(FORMAT))
            elif msg.startswith("TO_CLIENT:"):
                _, target_id, client_msg = msg.split(":", 2)
                target_id = int(target_id)
                if target_id in clients:
                    target_conn = clients[target_id]["conn"]
                    target_conn.send(f"Message from Client {client_id}: {client_msg}".encode(FORMAT))
                    conn.send(f"Message to Client {target_id} sent.".encode(FORMAT))
                else:
                    conn.send("Target client not found.".encode(FORMAT))
            else:
                print(f"[{addr}] {msg}")
                conn.send(f"Echo from server [Client {client_id}]: {msg}".encode(FORMAT))

    # Clean up client data on disconnect
    with lock:
        del clients[client_id]
    conn.close()
    print(f"[DISCONNECTED] {addr} (Client {client_id}) disconnected.")

# Allow server to listen for connections and handle clients
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:

        # Invokes when a new connection occurs
        conn, addr = server.accept()

        # When a new connection occurs, pass connection to handle_client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] Server is starting...")
start()