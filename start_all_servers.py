# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import time

import server_socket


def parse_input():
    parsed_input = []
    parsed_input.append(sys.argv[1])
    parsed_input.append(sys.argv[2])
    parsed_input.append(sys.argv[3])
    return parsed_input


def start_all_servers(own_datas):
    server_socket.start_server_socket(own_datas, sys.argv[4])


def start_program():
    own_datas = parse_input()
    start_all_servers(own_datas)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_program()
