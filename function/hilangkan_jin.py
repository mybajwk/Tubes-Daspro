import main_data
import builtin_function


def hilangkan_jin():
    delete_user = input("masukkan usernama jin: ")
    ditemukan = False
    for i in range(2, main_data.user_len):
        if main_data.data_csv_user[i][0] == delete_user:
            ditemukan = True
            confirm = input(
                f"Apakah anda yakin ingin menghapus jin dengan username {delete_user} (Y/N)? ")
            if confirm == "Y" or confirm == "y":
                for j in range(main_data.candi_len):
                    if main_data.data_csv_candi[j][1] == delete_user:
                        main_data.data_csv_candi, main_data.candi_len = builtin_function.hapus_data_list(
                            main_data.data_csv_candi, delete_user, main_data.candi_len, 1)
                main_data.data_csv_user[i] = ""
                main_data.user_len -= 1
                print("Jin berhasil dihapus dari alam gaib")
    if not ditemukan:
        print("Tidak ada jin dengan username tersebut.")
