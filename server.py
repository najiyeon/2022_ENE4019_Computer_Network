#2021038122 나지연

import socket
from _thread import*

clients = [] #list of clients connected to the server

#Server IP and Ports to open
HOST = '127.0.0.1'
PORT = 9999

#creating a Server Socket
print('>> Server Start')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

#code that runs on the thread
#A new thread is created for each connected client to communicate
def threaded(client, addr):
    print('Connected by : ', addr[0], ':', addr[1])

    #repeat until the client disconnects
    while True:
        try:
            #when the data is received, it is sent back to the client (Echo)
            data = client.recv(1024)

            if not data:
                print('Disconnected by ' + addr[0], ':', addr[1])
                break;

            print('Received from ' + addr[0], ':', addr[1], data.decode())

            #Send a message to a client who is connected to the server except for the person who sent the message
            for client_socket in clients :
                if client_socket != client :
                    client_socket.send(data)

        except ConnectionResetError as e:
            print('Disconnected by ' + addr[0], ':', addr[1])
            break

    if client in clients:
        clients.remove(client)
        print('remove client list : ', len(clients))

    client.close()

# when the client connects, the accept function returns a new socket

# new threads will communicate using their sockets

try:
    while True:
        print('Wait')

        client, addr = server.accept()
        clients.append(client)
        start_new_thread(threaded, (client, addr))
        print("Number of participants : ", len(clients))

except Exception as e:
    print('Error : ', e)

finally:
    server.close()