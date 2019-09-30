# Learning Python 101

from utils import *
import sys
import socket
import getopt
import select

HOST = '127.0.0.1'
PORT = 65432

class Server:
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = input("Enter a message: ")
                    if not data:
                        break
                    conn.sendall(data.encode())


class Client:
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((HOST, PORT))
            while True:
                socket_list = [s]
                read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

                for sock in read_sockets:
                    if sock == s:
                        data = s.recv(1024)
                        if data:
                            printf("Received: " + data.decode() + "\n")
                        else:
                            printf("Connection closed\n")
                            s.close()
                            return


def main():
    printf("Super simple server/client test\n")
    options, remainder =  getopt.getopt(sys.argv[1:], 'sc', ['server', 'client',])

    is_server = False
    is_client = False

    for opt, arg in options:
        if opt in ('-s', '--server'):
            is_server = True
        elif opt in ('-c', '--client'):
            is_client = True
        else:
            printf("Invalid option: " + str(opt) + "\n")
            return

    if is_server:
        printf("Working as server\n")
        server = Server()
        server.run()

    elif is_client:
        printf("Working as client\n")
        client = Client()
        client.run()

    else:
        printf("Not server nor client. Exiting now\n")


if __name__ == "__main__":
    main()
