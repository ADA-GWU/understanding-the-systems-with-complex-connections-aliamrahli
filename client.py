import socket
import random


def client_program():
    ports=[5000,5001,5002] # three different servers on these ports


    message = ''
    while message.strip() != 'stop': #program will continue untill user types stop
        port = random.choice(ports)
        host = socket.gethostname() # randomly chosing one of the servers
        # creating client socket
        client_socket = socket.socket()
        host = socket.gethostname()
        client_socket.connect((host, port))  # send connection request to server
        message = input(" -> ")  # take input from user
        client_socket.send(message.encode()) # send the input to server




if __name__ == '__main__':
    client_program()