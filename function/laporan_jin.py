
from builtin_function import push_back_data, push_back_data_list, getIndexList, loopSort
import main_data


def getJinfromJumlahCandi(data: list, data_len: int, value: int) -> tuple[list, int]:
    jinListlen = 0
    jinList = []
    for i in range(data_len):
        if data[i] == value:
            jinList = push_back_data(
                jinList, data[i], jinListlen)
            jinListlen += 1
    return jinList, jinListlen


def laporan_jin():
    total_jin = 0
    jin_pembangun = 0
    list_jin_pembuat_candi = []
    len_list_jin_pembuat_candi = 0
    jin_pengumpul = 0
    list_jumlah_candi = []
    pasir = 0
    air = 0
    batu = 0

    for i in range(main_data.user_len):
        if main_data.data_csv_user[i][2] == "jin_pengumpul" or main_data.data_csv_user[i][2] == "jin_pembangun":
            total_jin += 1
            if main_data.data_csv_user[i][2] == "jin_pengumpul":
                jin_pengumpul += 1
            elif main_data.data_csv_user[i][2] == "jin_pembangun":
                jin_pembangun += 1

    for i in range(main_data.candi_len):
        if getIndexList(list_jin_pembuat_candi, len_list_jin_pembuat_candi, main_data.data_csv_candi[i][1]) == -1:
            list_jin_pembuat_candi = push_back_data(
                list_jin_pembuat_candi, main_data.data_csv_candi[i][1], len_list_jin_pembuat_candi)
            list_jumlah_candi = push_back_data(
                list_jumlah_candi, 0, len_list_jin_pembuat_candi)
            len_list_jin_pembuat_candi += 1
        else:
            idx = getIndexList(list_jin_pembuat_candi,
                               len_list_jin_pembuat_candi, main_data.data_csv_candi[i][1])
            list_jumlah_candi[idx] = list_jumlah_candi[idx] + 1

    if jin_pembangun > 0:
        candi_min = loopSort(list_jumlah_candi, len_list_jin_pembuat_candi)[0]
        candi_max = loopSort(list_jumlah_candi, len_list_jin_pembuat_candi)[
            len_list_jin_pembuat_candi-1]
        kandidat_jin_terrajin, kandidat_jin_terrajin_len = getJinfromJumlahCandi(list_jumlah_candi, len_list_jin_pembuat_candi,
                                                                                 candi_max)
        kandidat_jin_termalas, kandidat_jin_termalas_len = getJinfromJumlahCandi(list_jumlah_candi, len_list_jin_pembuat_candi,
                                                                                 candi_min)

        if kandidat_jin_terrajin_len > 1:
            jin_terrajin = loopSort(kandidat_jin_terrajin)[0]
        else:
            jin_terrajin = kandidat_jin_terrajin[0]

        if kandidat_jin_termalas_len > 1:
            jin_termalas = loopSort(kandidat_jin_termalas)[
                kandidat_jin_termalas_len-1]
        else:
            jin_termalas = kandidat_jin_termalas[0]
    else:
        jin_terrajin = "-"
        jin_termalas = "-"

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
