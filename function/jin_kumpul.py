import main_data
from builtin_function import random_generator


def jin_kumpul():
    # lakukan pengumpulan candi dengan random generator buatan
    pasir = random_generator(0, 5)
    batu = random_generator(0, 5)
    air = random_generator(0, 5)
    # print jumlah bahan yang ditemukan
    print("Jin menemukan total",  pasir, " pasir,",
          batu, " batu, dan", air, " air.")
    # tambahkan ke data utama
    main_data.data_csv_bahan[1][2] = int(
        main_data.data_csv_bahan[1][2]) + pasir
    main_data.data_csv_bahan[2][2] = int(main_data.data_csv_bahan[2][2]) + batu
    main_data.data_csv_bahan[3][2] = int(main_data.data_csv_bahan[3][2]) + air
