import subprocess
import time
from sys import executable


import read_and_parse_datafile
import tools


rumor_counter_to_believ = 0


def start_all_servers(own_datas, path_to_data):
    print("__________________________")
    print(own_datas)
    subprocess.Popen([executable, 'start_all_servers.py', own_datas[0], own_datas[1], own_datas[2], path_to_data,
                      rumor_counter_to_believ], creationflags=subprocess.CREATE_NEW_CONSOLE)


def start_counting_server_for_servers_who_believe_rumor():
    subprocess.Popen([executable, 'server_count_servers_who_believe_rumor.py'],
                     creationflags=subprocess.CREATE_NEW_CONSOLE)


def start_program():
    path_to_data = tools.ask_for_path()
    parsed_data = read_and_parse_datafile.parse_data(path_to_data)
    global rumor_counter_to_believ
    rumor_counter_to_believ = tools.ask_for_counter_which_needs_for_believing()
    for x in range(0, len(parsed_data)):
        start_all_servers(parsed_data[x], path_to_data)
        time.sleep(0.1)

    #start_counting_server_for_servers_who_believe_rumor()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_program()
