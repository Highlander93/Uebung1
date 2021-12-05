# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys

import server_socket


def start_all_servers():
    server_socket.start_server_socket(sys.argv[1], sys.argv[2])


def start_program():
    start_all_servers()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_program()
