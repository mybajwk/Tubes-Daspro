import main_data


def exit():
    # masih belum ditentukan logout baru exit atau langsung exit
    opsi = input(
        "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    while (opsi != 'y' and opsi != 'n'):
        opsi = input(
            "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if opsi == 'y':
        print("saving")
        # make function for saving

    main_data.stop_program = True
