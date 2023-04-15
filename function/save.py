import main_data
import os


def save():
    name_file = input("masukkan nama folder ")
    if not os.path.exists(name_file):
        os.mkdir(name_file)
    file_user = open(name_file+"/user.txt", "w")
    user = ""
    for i in range(main_data.user_len):
        temp = ""
        for j in range(2):
            temp += main_data.data_csv_user[i][j]
            temp += ";"
        temp = temp + main_data.data_csv_user[i][2] + "\n"
        user += temp
    file_user.write(user)
    file_user.close()

    file_candi = open(f"{name_file}/candi.txt", "w")
    candi = ""
    for i in range(main_data.candi_len):
        temp = ""
        for j in range(4):
            temp += main_data.data_csv_candi[i][j]
            temp += ";"
        temp = temp + main_data.data_csv_candi[i][4] + "\n"
        candi += temp
    file_candi.write(candi)
    file_candi.close()

    file_bahan_bangunan = open(f"{name_file}/bahan_bangunan.txt", "w")
    bahan_bangunan = ""
    for i in range(4):
        temp = ""
        for j in range(2):
            temp += main_data.data_csv_bahan[i][j]
            temp += ";"
        temp = temp + main_data.data_csv_bahan[j][2] + "\n"
        bahan_bangunan += temp
    file_bahan_bangunan.write(bahan_bangunan)
    file_bahan_bangunan.close()
