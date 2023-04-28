from login import login
from load import read_file
from game import game
from help import command_help
from function.exit import exit
from builtin_function import notvalid
from load import read_file
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
    # load data dan save ke variabel global
    print("loading...")
    main_data.folder = folder_name
    read_file()
else:
    print("not found")
    main_data.stop_program = True


# main program
while not (main_data.stop_program):
    comand = input(">>> ")
    if not (main_data.is_login):
        if comand == "HELP":
            command_help(main_data.current_role)
        elif comand == "Login":
            while not (main_data.is_login):
                main_data.current_user, main_data.current_role, main_data.is_login = login()
        elif comand == "exit":
            exit()
        elif comand == "Logout":
            print("Logout gagal!")
            print(
                "Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        else:
            notvalid()

    while (main_data.is_login):
        comand = input("masukkan input ")
        game(comand)
