import main_data
from function.save import save


def exit():
    opsi = input(
        "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    while (opsi != 'y' and opsi != 'n' and opsi != 'Y' and opsi != 'N'):
        opsi = input(
            "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if opsi == 'y':
        # print("saving")
        save()
        # make function for saving
    main_data.stop_program = True
    main_data.is_login = False
