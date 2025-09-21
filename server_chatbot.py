import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Client: {message}")
        except:
            print("Connection closed by client.")
            break

def send_messages(client_socket):
    while True:
        try:
            message = input("You: ")
            client_socket.send(message.encode())
        except:
            print("Error sending message.")
            break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is listening on port 12345...")
client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")

# Start receiving and sending threads
threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
threading.Thread(target=send_messages, args=(client_socket,), daemon=True).start()

# Keep the main thread alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nServer shutting down.")
    client_socket.close()
    server_socket.close()