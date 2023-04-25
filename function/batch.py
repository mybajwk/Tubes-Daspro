import main_data
import random
import builtin_function


def get_id(data: list, len: int) -> int:
    id = 0
    for i in range(0, len):
        if (data[i] == None):
            id = i
    if id == 0:
        id = len+1
    return id


def batch_bangun():
    jin = 0  # jumlah jin
    data_jin = []
    for i in range(2, main_data.user_len):
        if (main_data.data_csv_user[i][2] == "jin_pembangun"):
            data_jin, jin = builtin_function.push_back_data_list(
                data_jin, main_data[i], jin)
    if (jin > 0):
        data_bahan = []
        total_pasir = 0
        total_batu = 0
        total_air = 0
        # kumpulkan bahan
        for i in range(jin):
            pasir = random.randint(1, 5)
            batu = random.randint(1, 5)
            air = random.randint(1, 5)
            total_pasir += pasir
            total_batu += batu
            total_air += air
            data_bahan, temp = builtin_function.push_back_data_list(
                data_bahan, [pasir, batu, air], i)
        print("Mengerahkan",  jin, " jin untuk membangun candi dengan total bahan",
              total_pasir, " pasir,", total_batu, " batu, dan", total_air, " air.")
        if int(main_data.data_csv_bahan[1][2]) >= pasir and int(main_data.data_csv_bahan[2][2]) >= batu and int(main_data.data_csv_bahan[3][2]) >= air:
            candi_terbangun = 0
            for i in range(jin):
                if (main_data.candi_len < 100):
                    id = get_id(main_data.data_csv_candi, main_data.candi_len)
                    add_candi = [id, data_jin[i][0], data_bahan[i]
                                 [0], data_bahan[i][1], data_bahan[i][2]]

                    main_data.data_csv_candi, main_data.candi_len = builtin_function.push_back_data_list(
                        main_data.data_csv_candi, add_candi, main_data.candi_len)
                candi_terbangun += 1
            print("Jin berhasil membangun total", candi_terbangun, " candi.")

        else:
            pasir_kurang = total_pasir-int(main_data.data_csv_bahan[1][2])
            batu_kurang = total_batu-int(main_data.data_csv_bahan[2][2])
            air_kurang = total_air-int(main_data.data_csv_bahan[3][2])
            print("Bangun gagal. Kurang", pasir_kurang, "pasir,",
                  batu_kurang, " batu, dan", air_kurang, " air.")

    else:
        print(
            "Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu")


def batch_kumpul():
    jin = 0
    for i in range(2, main_data.user_len):
        if (main_data.data_csv_user[i][2] == "jin_pengumpul"):
            jin += 1
    if (jin > 0):
        pasir = 0
        batu = 0
        air = 0
        print("mengerahkan", jin, " untuk mengumpulkan bahan.")
        for i in range(jin):
            pasir += random.randint(0, 5)
            batu += random.randint(0, 5)
            air += random.randint(0, 5)
        main_data.data_csv_bahan[1][2] = int(
            main_data.data_csv_bahan[1][2]) + pasir
        main_data.data_csv_bahan[2][2] = int(
            main_data.data_csv_bahan[2][2]) + batu
        main_data.data_csv_bahan[3][2] = int(
            main_data.data_csv_bahan[3][2]) + air

        print("Jin menemukan total",  pasir, " pasir,",
              batu, " batu, dan", air, " air.")

    else:
        print(
            "Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
