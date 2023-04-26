# from main_data import candi_len, data_csv_candi
import main_data


def laporan_candi():
    print(main_data.data_csv_candi)
    total = main_data.candi_len-1
    pasir = 0
    batu = 0
    air = 0
    idMax = 0
    idMin = 0
    max_harga = 0
    min_harga = 100000000
    for i in range(1, main_data.candi_len):
        pasir += int(main_data.data_csv_candi[i][2])
        batu += int(main_data.data_csv_candi[i][3])
        air += int(main_data.data_csv_candi[i][4])
        temp = 10000 * int(main_data.data_csv_candi[i][2]) + 15000 * int(
            main_data.data_csv_candi[i][3]) + 7500 * int(main_data.data_csv_candi[i][4])
        if max_harga < temp:
            idMax = main_data.data_csv_candi[i][0]
            max_harga = temp
        if min_harga > temp:
            idMin = main_data.data_csv_candi[i][0]
            min_harga = temp

    print("Total Candi:", total)

    print("Total Pasir yang digunakan:", pasir)
    print("Total Batu yang digunakan:", batu)
    print("Total Air yang digunakan:", air)
    if total > 0:
        print("ID Candi Termahal:", idMax, f"(Rp {max_harga})")
        print("ID Candi Termurah:", idMin, f"(Rp {min_harga})")
    else:
        print("ID Candi Termahal: -")
        print("ID Candi Termurah: -")
