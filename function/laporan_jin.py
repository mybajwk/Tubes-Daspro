
from builtin_function import push_back_data, push_back_data_list, getIndexList, loopSort
import main_data

def laporan_jin():
    total_jin = 0
    jin_pembangun = 0
    list_jin_pembuat_candi = []
    len_list_jin_pembuat_candi = 0
    jin_pengumpul = 0
    pasir = 0
    air = 0
    batu = 0
    # cari jin pembangun dan pengumpul
    for i in range(main_data.user_len):
        if main_data.data_csv_user[i][2] == "jin_pengumpul" or main_data.data_csv_user[i][2] == "jin_pembangun":
            total_jin += 1
            if main_data.data_csv_user[i][2] == "jin_pengumpul":
                jin_pengumpul += 1

            elif main_data.data_csv_user[i][2] == "jin_pembangun":
                jin_pembangun += 1
                # masukkan semua jin pembangun kedalam suatu array
                list_jin_pembuat_candi = push_back_data(
                    list_jin_pembuat_candi, [main_data.data_csv_user[i][0], 0], len_list_jin_pembuat_candi)
                len_list_jin_pembuat_candi += 1

    # pendataan setiap jin membangun berapa candi
    for i in range(1, main_data.candi_len):
        idx = getIndexList(list_jin_pembuat_candi,
                           len_list_jin_pembuat_candi, main_data.data_csv_candi[i][1])
        if idx != -1:
            list_jin_pembuat_candi[idx][1] += 1
        else:
            # handel jika dalam list candi ada pembuat yang merupakan jin pembangun yang udah dirubah ke jin pengumpul
            list_jin_pembuat_candi = push_back_data(
                list_jin_pembuat_candi, [main_data.data_csv_candi[i][1], 0], len_list_jin_pembuat_candi)
            len_list_jin_pembuat_candi += 1
            list_jin_pembuat_candi[idx][1] += 1

    if jin_pembangun > 0:
        # urutkan data berdasar jumlah candi dan leksikografis nama
        sort_data = loopSort(list_jin_pembuat_candi,
                             len_list_jin_pembuat_candi)
        jin_terrajin = sort_data[0][0]
        jin_termalas = sort_data[len_list_jin_pembuat_candi-1][0]

    else:
        jin_terrajin = "-"
        jin_termalas = "-"

    # mendata material yang ada saat ini
    for i in range(int(main_data.bahan_len)):
        if main_data.data_csv_bahan[i][0] == "pasir":
            pasir += int(main_data.data_csv_bahan[i][2])
        elif main_data.data_csv_bahan[i][0] == "batu":
            batu += int(main_data.data_csv_bahan[i][2])
        elif main_data.data_csv_bahan[i][0] == "air":
            air += int(main_data.data_csv_bahan[i][2])

    print("Total Jin:", total_jin)
    print("Total Jin Pengumpul:", jin_pengumpul)
    print("Total Jin Pembangun:", jin_pembangun)
    print("Jin Terajin:", jin_terrajin)
    print("Jin Termalas:", jin_termalas)
    print("Jumlah Pasir: {} unit".format(pasir))
    print("Jumlah Air: {} unit".format(air))
    print("Jumlah Batu: {} unit".format(batu))
