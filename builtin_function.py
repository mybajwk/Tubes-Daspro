import main_data
import time


def len_data(data: str) -> int:
    # pengganti len
    idx = 0
    for i in data:
        idx += 1
    return idx


def insertion_sort(arr, len):
    for i in range(2, len):
        key = arr[i]
        j = i - 1
        while j >= 1 and int(arr[j][0]) > int(key[0]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# push back data untuk string


def push_back_data(old_data: list, new_data: any, idx: int) -> list:
    # pengganti append
    idx += 1
    data_result = [None for k in range(idx)]
    for i in range(idx-1):
        data_result[i] = old_data[i]
    data_result[idx-1] = new_data

    return data_result

# hapus data list


def hapus_data_list(old_data: list, delete_data: str, len: int, posisi: int) -> tuple[list, int]:
    data_result = [None for k in range(len-1)]
    idx = 0
    for i in range(len):
        if not (old_data[i][posisi] == delete_data):
            data_result[idx] = old_data[i]
            idx += 1

    return data_result, len-1


# push back data untuk list


def push_back_data_list(old_data: list, new_data: list, len: int) -> tuple[list, int]:
    # pengganti append
    len += 1
    data_result = [None for k in range(len)]
    for i in range(len-1):
        data_result[i] = old_data[i]
    data_result[len-1] = new_data

    return data_result, len


def count_char(text, character):
    # menghitung jumlah char yang dicari dalam suatu kata
    idx = 0
    for i in text:
        if i == character:
            idx += 1
    return idx


def csv_reader(data: list, delimiter: str) -> tuple[list, int]:
    result = []
    length_data = 0
    for line in data:
        data_line = []
        last_word = False
        idx = 0
        word = ""
        for character in line:
            if character == "\n":
                last_word = True
            if character == delimiter:
                data_line = push_back_data(data_line, word, idx)
                word = ""
                idx += 1
            else:
                if not (last_word):
                    word += character
        data_line = push_back_data(data_line, word, idx)
        result = push_back_data(result, data_line, length_data)
        length_data += 1
    return result, length_data


def getIndexList(data: list, data_len: int, search: str) -> int:
    for i in range(data_len):
        if data[i][0] == search:
            return i
    return -1


def loopSort(data: list, data_len: int) -> list:
    for i in range(data_len):
        for j in range(data_len-1):
            if data[j][1] < data[j+1][1]:
                temp = data[j+1]
                data[j+1] = data[j]
                data[j] = temp
            elif data[j][1] == data[j+1][1]:
                if data[j][0] > data[j+1][0]:
                    temp = data[j+1]
                    data[j+1] = data[j]
                    data[j] = temp
    return data


def notvalid():
    print("invalid command")


def unauthorized(role):
    print(f"{role} tidak memiliki akses pada command ini.")


def random_generator(start: int, end: int) -> int:
    seed = int(time.time())
    a = 567125673
    c = 1
    m = end
    condition = True
    while condition:
        time.sleep(float((seed % 10)/10))
        seed += int(time.time())
        LCG = ((a*seed)+c) % m
        seed = seed + 1
        if LCG >= start and LCG <= end:
            return LCG
