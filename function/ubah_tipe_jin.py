import main_data


def ubah_tipe_jin():
    valid = False
    while not valid:
        username = input("Masukkan username jin :")
        idx = 0
        for i in main_data.user_data:
            if (username != main_data.user_data[0]):
                idx += 1
            else:
                valid = True
        if not valid:
            print("Tidak ada jin dengan username tersebut.")
        else:
            if (main_data.user_data[2] == "jin_pengumpul"):
                print(
                    'Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun"')
            else:
                print()
