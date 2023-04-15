from main_data import candi_len, data_csv_candi


def laporan_candi():
    total = candi_len
    pasir = 0
    batu = 0
    air = 0
    idMax = 0
    idMin = 0
    max_harga = 0
    min_harga = 100000000
    for i in range(candi_len):
        pasir += data_csv_candi[i][2]
        batu += data_csv_candi[i][3]
        air += data_csv_candi[i][4]
        temp = 10000 * pasir + 15000 * batu + 7500 * air
        if max_harga < temp:
            max_harga = temp
        elif min_harga > temp:
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
