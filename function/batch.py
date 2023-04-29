import main_data
import builtin_function
from builtin_function import insertion_sort, random_generator


def get_id(data: list, len: int) -> int:
    id = 1
    while (id < len):
        if (int(data[id][0]) > id):
            break
        id += 1

    return id


def batch_bangun():
    jin = 0  # jumlah jin
    data_jin = []
    for i in range(2, main_data.user_len):
        if (main_data.data_csv_user[i][2] == "jin_pembangun"):
            data_jin, jin = builtin_function.push_back_data_list(
                data_jin, main_data.data_csv_user[i], jin)
    if (jin > 0):
        data_bahan = []
        total_pasir = 0
        total_batu = 0
        total_air = 0
        # kumpulkan bahan
        for i in range(jin):
            pasir = random_generator(1, 5)
            batu = random_generator(1, 5)
            air = random_generator(1, 5)
            total_pasir += pasir
            total_batu += batu
            total_air += air
            data_bahan, _ = builtin_function.push_back_data_list(
                data_bahan, [pasir, batu, air], i)
        print("Mengerahkan",  jin, "jin untuk membangun candi dengan total bahan",
              total_pasir, " pasir,", total_batu, "batu, dan", total_air, "air.")
        if int(main_data.data_csv_bahan[1][2]) >= pasir and int(main_data.data_csv_bahan[2][2]) >= batu and int(main_data.data_csv_bahan[3][2]) >= air:
            candi_terbangun = 0

            main_data.data_csv_bahan[1][2] = int(
                main_data.data_csv_bahan[1][2]) - total_pasir
            main_data.data_csv_bahan[2][2] = int(
                main_data.data_csv_bahan[2][2]) - total_batu
            main_data.data_csv_bahan[3][2] = int(
                main_data.data_csv_bahan[3][2]) - total_air
            for i in range(jin):
                if (main_data.candi_len < 100):
                    main_data.data_csv_candi = insertion_sort(
                        main_data.data_csv_candi, main_data.candi_len)
                    id = get_id(main_data.data_csv_candi,
                                int(main_data.candi_len))
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
            if (total_pasir < int(main_data.data_csv_bahan[1][2])):
                pasir_kurang = 0
            if (total_batu < int(main_data.data_csv_bahan[2][2])):
                batu_kurang = 0
            if (total_air < int(main_data.data_csv_bahan[3][2])):
                air_kurang = 0

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
        print("mengerahkan", jin, "jin untuk mengumpulkan bahan.")
        for i in range(jin):
            pasir += random_generator(0, 5)
            batu += random_generator(0, 5)
            air += random_generator(0, 5)
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
