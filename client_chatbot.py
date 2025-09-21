import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(f"Server: {message}")
        except:
            print("Connection closed by server.")
            break

def send_messages(sock):
    while True:
        try:
            message = input("You: ")
            sock.send(message.encode())
        except:
            print("Error sending message.")
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Start receiving and sending threads
threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
threading.Thread(target=send_messages, args=(client_socket,), daemon=True).start()

# Keep the main thread alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nClient shutting down.")
    client_socket.close()
