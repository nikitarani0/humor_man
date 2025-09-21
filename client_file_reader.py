import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Step 1: Send filename
filename = input("Enter the filename (e.g., 'sample.txt'): ")
client_socket.send(filename.encode())

# Step 2: Receive response
response = client_socket.recv(4096).decode()

print(response)

client_socket.close()
