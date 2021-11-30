import socket


def start_server_socket(endpoint):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Waiting for client ...')
    serversocket.bind((endpoint[0], int(endpoint[1])))
    serversocket.listen(0)

    (clientsocket, adress) = serversocket.accept()
    print('client connected')

    while True:
        msg = clientsocket.recv(1024)
        msg = msg.decode()
        print('Message: ' + msg)

        ans = 'Message: ' + msg
        ans = ans.encode()
        clientsocket.send(ans)

    clientsocket.close()
    serversocket.close()