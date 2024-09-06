import argparse
import socket
from queue import Queue
from threading import Thread, Lock
from colorama import init, Fore


init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

N_THREADS = 200
q = Queue()
print_lock = Lock()

def port_scan(port):

    try:
        s=socket.socket()
        s.connect((host, port))
    except:
        with print_lock:
            print(f'{GRAY}{host:15}:{port:5} is closed {RESET}')
    else:
        with print_lock:
            print(f'{GREEN}{host:15}:{port:5} is open {RESET}')

    finally:
        s.close()

def scan_thread():
    global q
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()


def main(host, ports):
    for i in range(N_THREADS):
        i = Thread(target=scan_thread)
        i.daemon = True
        i.start()
    for worker in ports:
        q.put(worker)
    q.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Threaded port scanner")
    parser.add_argument("host", help="Host to scan (e.g., localhost or google.com)")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, default is 1-65535 (all ports)")
    args = parser.parse_args()
    host, port_range = args.host, args.port_range

    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)

    ports = [ p for p in range(start_port, end_port) ]

    main(host, ports)
