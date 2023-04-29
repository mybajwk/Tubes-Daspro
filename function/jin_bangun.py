import main_data
import builtin_function
from builtin_function import random_generator


def get_id(data: list, len: int) -> int:
    # untuk menentukan id data selanjutnya yang hendak di buat
    id = 1
    for i in range(2, len):
        if (data[id][0]+1 < data[i][0]):
            id = data[id][0]+1
        id += 1
    if id == 1:
        id = len+1
    return id


def jin_bangun():
    # random pasir, batu, air dengan randomg enerator number
    pasir = random_generator(1, 5)
    batu = random_generator(1, 5)
    air = random_generator(1, 5)
    # cek apakah bahan yang dibutuhkan cukup
    if int(main_data.data_csv_bahan[1][2]) >= pasir and int(main_data.data_csv_bahan[2][2]) >= batu and int(main_data.data_csv_bahan[3][2]) >= air:
        print("Candi berhasil dibangun")
        # jika candi masih kurang dari 100 maka bangun  jika tidak skip saja
        if (main_data.candi_len <= 100):
            # cek id
            id = get_id(main_data.data_csv_candi, int(main_data.candi_len))
            # simpan data candi dalam array lalu tambahkan array ke data utamaa
            add_candi = [id, main_data.current_user, pasir, batu, air]
            main_data.data_csv_candi, main_data.candi_len = builtin_function.push_back_data_list(
                main_data.data_csv_candi, add_candi, main_data.candi_len)
        print("Sisa candi yang perlu dibangun:", 100-main_data.candi_len+1)
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
