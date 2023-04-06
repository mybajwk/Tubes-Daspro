import main_data


def ubah_tipe_jin():
    valid = False
    while not valid:
        username = input("Masukkan username jin :")
        idx = 0
        for i in main_data.data_csv_user:
            if (username != i[0]):
                idx += 1
            else:
                valid = True
        if not valid:
            print("Tidak ada jin dengan username tersebut.")
        else:
            choice = None
            change_to = None
            if (main_data.user_data[2] == "jin_pengumpul"):
                change_to = "jin_pembangun"
                choice = input(
                    'Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)')
            else:
                change_to = "jin_pengumpul"
                choice = input(
                    'Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "pengumpul" (Y/N)')

            if choice == 'Y':
                main_data.data_csv_user[idx][2] = change_to
                print(main_data.data_csv_user)
                print("Jin telah berhasil diubah.")
            elif choice == "N":
                print("Jin tidak jadi diubah")
            else:
                print("opsi salah")
