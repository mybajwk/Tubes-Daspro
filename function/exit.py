import main_data
from function.save import save


def exit():
    # masih belum ditentukan logout baru exit atau langsung exit
    if main_data.current_role == "roro_jonggrang" or main_data.current_role == "bandung_bondowoso":
        opsi = input(
            "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        while (opsi != 'y' and opsi != 'n'):
            opsi = input(
                "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        if opsi == 'y':
            # print("saving")
            save()
            # make function for saving

    main_data.stop_program = True
