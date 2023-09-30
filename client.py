import socket


def client_program():
    # creating client socket
    client_socket = socket.socket()
    host = socket.gethostname()
    client_socket.connect((host, 5000))  # send connection request to server
    message = ''
    while message.strip() != 'stop': #program will continue untill user types stop
        message = input(" -> ")  # take input from user
        client_socket.send(message.encode()) # send the input to server




if __name__ == '__main__':
    client_program()