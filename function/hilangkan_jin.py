import main_data


def hilangkan_jin():
    delete_user = input("masukkan usernama jin: ")
    ditemukan = False
    for i in range(1, main_data.user_len):
        if main_data.data_csv_user[i][0] == delete_user:
            ditemukan = True
            confirm = input(
                "Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
            if confirm == "Y":
                main_data.data_csv_user[i] = "\n"
    if not ditemukan:
        print("Tidak ada jin dengan username tersebut.")
    print(main_data.data_csv_user)
