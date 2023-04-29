import main_data
import os
from builtin_function import insertion_sort


def save():
    # melakukan saving user.csv
    name_file = input("masukkan nama folder ")
    print("Saving...")
    if not os.path.exists(name_file):
        os.makedirs(name_file)
        print(f"Membuat folder {name_file}...")
    file_user = open(name_file+"/user.csv", "w")
    user = ""
    for i in range(main_data.user_len):
        temp = ""
        for j in range(2):
            # rubah semua data kedalam string yang dipisahkan oleh ";"
            temp += str(main_data.data_csv_user[i][j])
            temp += ";"
        temp = temp + str(main_data.data_csv_user[i][2]) + "\n"
        user += temp
    file_user.write(user)
    file_user.close()

    # melakukan saving data candi
    # sorting id candi dulu
    main_data.data_csv_candi = insertion_sort(
        main_data.data_csv_candi, main_data.candi_len)

    file_candi = open(f"{name_file}/candi.csv", "w")
    candi = ""
    for i in range(main_data.candi_len):
        temp = ""
        for j in range(4):
            # rubah semua data kedalam string yang dipisahkan oleh ";"
            temp += str(main_data.data_csv_candi[i][j])
            temp += ";"
        temp = str(temp + str(main_data.data_csv_candi[i][4])) + "\n"
        candi += temp
    file_candi.write(candi)
    file_candi.close()

    # melakukan saving data bahan bangunan
    file_bahan_bangunan = open(f"{name_file}/bahan_bangunan.csv", "w")
    bahan_bangunan = ""
    for i in range(4):
        temp = ""
        for j in range(2):
            # rubah semua data kedalam string yang dipisahkan oleh ";"
            temp += str(main_data.data_csv_bahan[i][j])
            temp += ";"
        temp = temp + str(main_data.data_csv_bahan[i][2]) + "\n"
        bahan_bangunan += temp
    file_bahan_bangunan.write(bahan_bangunan)
    file_bahan_bangunan.close()
    print(f"Berhasil menyimpan data di folder {name_file}!")
