#2021038122 나지연

import socket
from _thread import*

HOST = '127.0.0.1'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# method to receive messages from the server
# Thread-driven to work separately from the code sending the message
def recv_data(client):
    while True:
        data = client.recv(1024)

        print('recieve : ', repr(data.decode()))

start_new_thread(recv_data, (client,))
print('Connect Server')

while True:
    message = input('')
    if message == 'quit':
        close_data = message
        break

    client.send(message.encode())

client.close()