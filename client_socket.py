import socket


def start_client_socket():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('127.0.0.1', 2712))

    while True:
        print('Bitte eine Message schreiben: ')
        msg = input()
        msg = msg.encode()
        clientsocket.send(msg)

        msg = clientsocket.recv(1024)
        msg = msg.decode()
        print('Serverantwort: ' + msg)

    clientsocket.close()


if __name__ == '__main__':
    start_client_socket()
