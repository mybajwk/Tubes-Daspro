from login import login
from load import read_file
from game import game
import main_data
import argparse
import os

# load folder directory for first time
parser = argparse.ArgumentParser()
parser.add_argument("name", type=str,
                    help="input for load folder name", nargs='?', const='')
args = parser.parse_args()
folder_name = args.name
if folder_name == None:
    print("tidak ada input")
    main_data.stop_program = True
elif os.path.isdir(folder_name):
    print("loading...")
    main_data.folder = folder_name
else:
    print("not found")
    main_data.stop_program = True

# main program
while not (main_data.stop_program):
    comand = input("masukkan input ")
    if not (main_data.is_login):
        match comand:
            case "HELP":
                help(main_data.current_role)
            case "login":
                while not (main_data.is_login):
                    main_data.current_user, main_data.current_role, main_data.is_login = login()
            case "load":
                file_name = input("nama file ")
                read_file(file_name)
    if (main_data.is_login):
        game()
