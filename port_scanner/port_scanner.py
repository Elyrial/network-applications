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
    # Empty list to store hosts with open port
    open_port_list = []

    host_address = input("Enter the host (e.g., localhost or google.com): ")

    # Iterate ports from 1 to 512
    for port in range(1, 513):
        # Only prints out when the port is open
        if is_port_open(host_address, port):
            print(f'{GREEN}[+] {host_address}:{port} is open {RESET}')
            open_port_list.append(port)
        else:
            print(f'{GRAY}[!] {host_address}:{port} is closed {RESET}')

    # Print out all open ports
    for index, open_port in enumerate(open_port_list, start=1):
        print(f'{index}. PORT {GREEN}{open_port}{RESET} is open')

if __name__ == "__main__":
    main()
