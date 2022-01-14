import subprocess
from sys import executable


import read_and_parse_datafile
import tools


def start_all_servers(own_datas, path_to_data):
    print("____________________")
    print(own_datas)
    subprocess.Popen([executable, 'start_all_servers.py', own_datas[0], own_datas[1], own_datas[2], path_to_data],
                     creationflags=subprocess.CREATE_NEW_CONSOLE)


def start_counting_server_for_servers_who_believe_rumor():
    subprocess.Popen([executable, 'server_count_servers_who_believe_rumor.py'],
                     creationflags=subprocess.CREATE_NEW_CONSOLE)


def start_program():
    path_to_data = tools.ask_for_path()
    parsed_data = read_and_parse_datafile.parse_data(path_to_data)

    for x in range(0, len(parsed_data)):
        start_all_servers(parsed_data[x], path_to_data)

    #start_counting_server_for_servers_who_believe_rumor()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_program()
