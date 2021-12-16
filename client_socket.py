import socket
from datetime import datetime


def start_client_socket():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('127.0.0.1', 5001))
    print('Bitte eine Message schreiben: ')
    msg = input()
    msg = msg.encode()
    clientsocket.send(msg)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%f")
    print("Current Time =", current_time)

    clientsocket.close()


if __name__ == '__main__':
    start_client_socket()
