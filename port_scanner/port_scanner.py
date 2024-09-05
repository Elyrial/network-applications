import socket
from colorama import init, Fore

# User friendly colors for prompt readability
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def is_port_open(host, port):

    # Create socket
    s = socket.socket()

    # Set a timeout for the socket
    s.settimeout(0.05)

    try:
        # Try to connect to the host using the give port
        s.connect((host, port))

    # Return false if connection fails
    except:
        return False

    # Return true if connection is established
    else:
        return True

def main():
    host_address = input("Enter the host (e.g., localhost or google.com): ")

    # Iterate ports from 1 to 512
    for port in range(1, 513):
        # Only prints out when the port is open
        if is_port_open(host_address, port):
            print(f'{GREEN}[+] {host_address}:{port} is open {RESET}')
        else:
            print(f'{GRAY}[!] {host_address}:{port} is closed {RESET}')

if __name__ == "__main__":
    main()
