from datetime import datetime


def ask_for_path():
    # Use a breakpoint in the code line below to debug your script.
    print('Please insert path to data: ', end="")
    # path_to_data = input()
    return "C:\\Users\\Müller\\PycharmProjects\\Uebung1\\PfadZurDatei\\data.txt"
    # return "C:\\Users\\muell\\PycharmProjects\\Uebung1\\PfadZurDatei\\data.txt"


def ask_for_id():
    print('Please insert ID: ', end="")
    return input()


def ask_for_counter_which_needs_for_believing():
    print('Please insert Anzahl an Server von denen man ein Gerücht hören muss um dieses zu glauben: ', end="")
    return input()


def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S:%f")
