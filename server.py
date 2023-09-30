import socket


def server_program():

       # creating server socket and binding the host and port number
       host = socket.gethostname() #
       server_socket = socket.socket()
       server_socket.bind((host, 5000))

       #server is listening to one client simultaneously
       server_socket.listen(1)

       conn, address = server_socket.accept() #accepting the connection request from client
       print("Successfully connected to: " + str(address))

       data = conn.recv(1024).decode() #getting data sent by client
       print("Message from client: " + str(data))


if __name__ == '__main__':
    server_program()