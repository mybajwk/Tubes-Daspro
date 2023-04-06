import main_data


def len_data(data):
    # pengganti len
    idx = 0
    for i in data:
        idx += 1
    return idx


def push_back_data(old_data, new_data):
    # pengganti append
    idx = len_data(old_data)
    idx += 1
    data_result = [None for k in range(idx)]
    for i in range(idx-1):
        data_result[i] = old_data[i]
    data_result[idx-1] = new_data

    return data_result


def count_char(text, character):
    # menghitung jumlah char yang dicari dalam suatu kata
    idx = 0
    for i in text:
        if i == character:
            idx += 1
    return idx


def csv_reader(data, delimiter):
    result = []
    for line in data:
        data_line = []
        last_word = False
        idx = 0
        word = ""
        for character in line:
            if character == "\n":
                last_word = True
            if character == delimiter:
                data_line = push_back_data(data_line, word)
                word = ""
            else:
                if not (last_word):
                    word += character
            idx += 1
        data_line = push_back_data(data_line, word)
        result = push_back_data(result, data_line)
    return result
    # tambahan fitur bonus
    # def random():
