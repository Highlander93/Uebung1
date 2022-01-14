from datetime import datetime


def ask_for_path():
    # Use a breakpoint in the code line below to debug your script.
    print('Please insert path to data: ')
    # path_to_data = input()
    return "C:\\Users\\Müller\\PycharmProjects\\Uebung1\\PfadZurDatei\\data.txt"
    # return "C:\\Users\\muell\\PycharmProjects\\Uebung1\\PfadZurDatei\\data.txt"


def ask_for_id():
    print('Please insert ID: ')
    return input()


def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S:%f")
