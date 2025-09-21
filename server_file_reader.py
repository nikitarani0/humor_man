import socket
import re

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server listening on port 12345...")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Receive filename from client
filename = client_socket.recv(1024).decode()
print(f"Requested file: {filename}")

try:
    with open(filename, 'r') as file:
        response = file.read()
except FileNotFoundError:
    response = "ERROR: File not found."
except Exception as e:
    response = f"ERROR: {str(e)}"

client_socket.send(response.encode())
client_socket.close()
server_socket.close()
