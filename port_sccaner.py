import socket

def scan_ports(target_host, start_port, end_port):
    """
    Scans a range of ports on a target host and prints open ports.
    """
    print(f"Scanning ports {start_port}-{end_port} on {target_host}...")
    for port in range(start_port, end_port + 1):
        try:
            # Create a new socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt
            sock.settimeout(1)  # 1 second timeout

            # Attempt to connect to the target host and port
            result = sock.connect_ex((target_host, port))

            if result == 0:
                print(f"Port {port} is OPEN")
            
            sock.close() # Close the socket after each attempt

        except socket.error as e:
            print(f"Error scanning port {port}: {e}")
        except KeyboardInterrupt:
            print("\nExiting port scanner.")
            break

if __name__ == "__main__":
    target = input("Enter the target host (IP address or hostname): ")
    start = int(input("Enter the starting port number: "))
    end = int(input("Enter the ending port number: "))

    scan_ports(target, start, end)