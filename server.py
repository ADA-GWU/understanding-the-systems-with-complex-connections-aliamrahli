import socket
import sys


def server_program():
    while True:
        # creating server socket and binding the host and port number
        host = socket.gethostname()
        server_socket = socket.socket()
        server_socket.bind((host, port))

        conn, address = server_socket.accept()  # accepting the connection request from client
        print("Successfully connected to: " + str(address))

        data = conn.recv(1024).decode()  # getting data sent by client

        if str(data) == 'exit':
            print('Connection closed')
            break

        if not data.isdigit():
            print('This program works only with digits!')
            continue
        else:
            new_data = 2 * int(data)
        print("Message from client: " + str(new_data))


if __name__ == '__main__':
    port = int(sys.argv[1])  # take port number of server as an argument
    server_program()
