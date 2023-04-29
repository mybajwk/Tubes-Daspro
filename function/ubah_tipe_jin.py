import main_data


def ubah_tipe_jin():
    valid = False
    idx = 0
    while not valid and idx < 3:
        # menerima masukan username jin dan akan terus looping maksimal 3 kali untuk handel apabila blm ada jin sama sekali
        username = input("Masukkan username jin: ")
        idx = 0
        # ceusername jin ada ataua tidak
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
            if (main_data.data_csv_user[idx][2] == "jin_pengumpul"):
                change_to = "jin_pembangun"
                choice = input(
                    'Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)')
            else:
                change_to = "jin_pengumpul"
                choice = input(
                    'Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "pengumpul" (Y/N)')
            # ubah data jin
            if choice == 'Y' or choice == "y":
                main_data.data_csv_user[idx][2] = change_to
                print("Jin telah berhasil diubah.")
            elif choice == "N" or choice == "n":
                print("Jin tidak jadi diubah")
            else:
                print("opsi salah")
    idx += 1
