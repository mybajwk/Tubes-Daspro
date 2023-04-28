import main_data
import builtin_function


def hancurkan_candi():
    id_candi = input("Masukkan ID candi: ")
    is_candi_ada = False
    row = 0
    for i in range(1, main_data.candi_len):
        if main_data.data_csv_candi[i][0] == id_candi:
            is_candi_ada = True
            row = i
            break

    if is_candi_ada == True:
        konfirmasi = input(
            f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")
        if konfirmasi == 'Y' or konfirmasi == "y":
            main_data.data_csv_candi, main_data.candi_len = builtin_function.hapus_data_list(
                main_data.data_csv_candi, id_candi, main_data.candi_len, 0)

            print("\nCandi telah berhasil dihancurkan")
    else:
        print("Tidak ada candi dengan ID tersebut.")
