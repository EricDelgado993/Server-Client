###### [↩️Return to Portfolio](https://github.com/EricDelgado993/Portfolio)
# Client-Server Communication Program

## Overview
The **Client-Server Communication Program** demonstrates a basic client-server architecture, enabling two-way communication between a server and multiple clients. The server listens for incoming connections and processes client requests, facilitating real-time data exchange and controlled interactions. This program serves as an excellent example of fundamental networking and socket programming principles.

---

## 📂 Project Files
- [Server Program](https://github.com/EricDelgado993/Server-Client/blob/main/Client%20Server%20Program/Server.py) - Implements server-side logic for handling client connections and processing requests.
- [Client Program](https://github.com/EricDelgado993/Server-Client/blob/main/Client%20Server%20Program/Client.py) - Provides the client-side interface to connect with the server and send commands.
- [Demo Video](https://github.com/EricDelgado993/Server-Client/blob/main/Client%20Server%20Program/Demo.mp4) -  A visual demonstration of the program in action.

---

## Features

###  Multi-Client Support
- Allows multiple clients to connect to the server simultaneously.

### Two-Way Communication
- Clients can send requests, and the server responds with relevant data.

### Message Broadcasting
- The server can broadcast messages to all connected clients.

### Error Handling
- Includes basic error handling to manage:
  - Unexpected client disconnections.
  - Invalid or malformed requests.

### Custom Commands
- Supports predefined commands for specific actions, such as:
  - `ping`: Checks server responsiveness.
  - `broadcast`: Sends a message to all connected clients.
  - `shutdown`: Gracefully terminates the server.

### Connection Logging
- Logs events such as:
  - Client connections and disconnections.
  - Messages exchanged between the server and clients.

### Secure Communication
- Optionally uses basic encryption to secure data transfer between clients and the server.

---

## How It Works

1. **Start the Server**: 
   - The server listens for incoming client connections on a specified port.
2. **Connect Clients**: 
   - Clients connect to the server using the server's address and port.
3. **Exchange Messages**: 
   - Clients send requests, and the server responds accordingly.
4. **Broadcast Communication**: 
   - The server can send a message to all connected clients simultaneously.
5. **Log Activities**: 
   - Connections, disconnections, and message exchanges are logged for tracking.
