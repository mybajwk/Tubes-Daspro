import main_data
from help import command_help


def notvalid():
    print("invalid command")


def unauthorized():
    print("unauthorized command")


def game():
    # print(main_data.current_role, main_data.current_user)
    current_role = main_data.current_role
    while (main_data.is_login):
        x = input()
        match x:
            case "HELP":
                command_help(current_role)
            case "Summon Jin":
                if (current_role == "bandung_bondowoso"):
                    command_help(current_role)
                else:
                    unauthorized()
            case "Hilangkan Jin":
                if (current_role == "bandung_bondowoso"):
                    command_help(current_role)
                else:
                    unauthorized()
            case "Ubah Tipe Jin":
                if (current_role == "bandung_bondowoso"):
                    command_help(current_role)
                else:
                    unauthorized()
            case "Bangun":
                if (current_role == "jin_pembangun"):
                    command_help(current_role)
                else:
                    unauthorized()
            case "Kumpul":
                if (current_role == "jin_pengumpul"):
                    command_help(current_role)
                else:
                    unauthorized()
            case "Batch Kumpul":
                if (current_role == "bandung_bondowoso"):
                    command_help(current_role)
                else:
                    unauthorized()
            case "Batch Bangun":
                if (current_role == "bandung_bondowoso"):
                    command_help(current_role)
                else:
                    unauthorized()
            case "Laporan Jin":
                if (current_role == "bandung_bondowoso"):
                    command_help(current_role)
                else:
                    unauthorized()
            case "Laporan Candi":
                if (current_role == "bandung_bondowoso"):
                    command_help(current_role)
                else:
                    unauthorized()
            case "Hancurkan Candi":
                if (current_role == "roro_jonggrang"):
                    command_help(current_role)
                else:
                    unauthorized()
            case "Ayam Berkokok":
                if (current_role == "roro_jonggrang"):
                    command_help(current_role)
                else:
                    unauthorized()

            case "Exit":
                confirm = input(
                    "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
                while not (confirm == 'y' or confirm == 'n'):
                    confirm = input(
                        "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
                if confirm == 'y':
                    # lakukan save
                    print("save")
                else:
                    main_data.current_role = None
                    main_data.current_user = None
                    main_data.is_login = False
                    main_data.stop_program = True
            case "logout":
                main_data.current_role = None
                main_data.current_user = None
                main_data.is_login = False
            case _:
                notvalid()
