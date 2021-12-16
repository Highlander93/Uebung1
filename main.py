# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess
from sys import executable

from graphviz import Source

import read_and_parse_datafile


def ask_for_path():
    # Use a breakpoint in the code line below to debug your script.
    print('Please insert path to data:')
    # path_to_data = input()
    return "C:\\Users\\Müller\\PycharmProjects\\Uebung1\\PfadZurDatei\\data.txt"
    # return "C:\\Users\\muell\\PycharmProjects\\Uebung1\\PfadZurDatei\\data.txt"


def start_all_servers(own_datas, path_to_data):
    print("____________________")
    print(own_datas)
    subprocess.Popen([executable, 'start_all_servers.py', own_datas[0], own_datas[1], own_datas[2], path_to_data],
                     creationflags=subprocess.CREATE_NEW_CONSOLE)


def start_counting_server_for_servers_who_believe_rumor():
    subprocess.Popen([executable, 'server_count_servers_who_believe_rumor.py'],
                     creationflags=subprocess.CREATE_NEW_CONSOLE)


def start_program():
    path_to_data = ask_for_path()
    parsed_data = read_and_parse_datafile.parse_data(path_to_data)

    for x in range(0, len(parsed_data)):
        start_all_servers(parsed_data[x], path_to_data)

    #start_counting_server_for_servers_who_believe_rumor()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_program()
