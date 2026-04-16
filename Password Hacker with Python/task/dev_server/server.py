import socket
from typing import Final

BUFFER_SIZE: Final[int] = 1024

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        print("Server started")
        server_socket.bind(('localhost', 9090))
        server_socket.listen(1)
        while True:
            conn, addr = server_socket.accept()
            print(f"Connected {addr}")
            while True:
                request = conn.recv(BUFFER_SIZE).decode()

                if not request:
                    print(f"Client {addr} is gone.")
                    break

                print(f"Received {request}")

                if request == "goodPass":
                    conn.send("Connection Success!".encode())
                else:
                    conn.send("Wrong password!".encode())


if __name__ == "__main__":
    run_server()