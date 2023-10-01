import socket
import random


def client_program():
    ports = [5000, 5001, 5002]  # three different servers on these ports
    flag = 0
    print('Type exit to stop the program')
    while len(ports) != 0:  # program will continue until user types stop
        port = random.choice(ports)  # randomly choosing one of the servers

        # creating client socket
        client_socket = socket.socket()
        host = socket.gethostname()

        client_socket.connect((host, port))  # send connection request to server
        message = input(" -> ")  # take input from user

        if len(ports) == 0:
            print('Application stopped! See you later :)')
            break

        client_socket.send(message.encode())  # send the input to server

        if message == 'exit':
            ports.remove(port)


if __name__ == '__main__':
    client_program()
