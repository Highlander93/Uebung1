# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import server_socket


def ask_for_path():
    # Use a breakpoint in the code line below to debug your script.
    print('Please insert path to data:')
    # path_to_data = input()
    # return "C:\\Users\\Müller\\PycharmProjects\\Uebung1\\PfadZurDatei\\data.txt"
    return "C:\\Users\\muell\\PycharmProjects\\Uebung1\\PfadZurDatei\\data.txt"


def ask_for_unique_id():
    print('Please insert the unique ID for this program:')
    # unique_id = input()
    return "3"


def parse_data(path_to_data):
    file = open(path_to_data)
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
    mapped_lines = dict(map(map_lines, nonempty_lines))
    file.close()
    return mapped_lines


def map_lines(nonempty_lines):
    mapping_between_space = nonempty_lines.split(" ")
    mapping_result = mapping_between_space[1].split(":")
    return mapping_between_space[0], (mapping_result[0], mapping_result[1])


def start_program():
    path_to_data = ask_for_path()
    unique_id = ask_for_unique_id()
    parsed_data = parse_data(path_to_data)
    server_socket.start_server_socket(parsed_data[unique_id])
    print(parsed_data[unique_id])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_program()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
