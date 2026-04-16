import sys
import socket

BUFFER_SIZE = 1024

def run_hacker_app():
    if (len(sys.argv) < 4):
        print("Usage: python hack.py <ip> <port> <password>")
        return

    ip = sys.argv[1]
    port = int(sys.argv[2])
    password = sys.argv[3]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.send(password.encode())
        response = s.recv(BUFFER_SIZE).decode()
        print(response)

if __name__ == '__main__':
    run_hacker_app()