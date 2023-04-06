import main_data


def len_data(data):
    idx = 0
    for i in data:
        idx += 1
    return idx


def push_back_data(old_data, new_data):
    idx = len_data(old_data)
    idx += 1
    data_result = [None for k in range(idx)]
    for i in range(idx-1):
        data_result[i] = old_data[i]
    data_result[idx-1] = new_data

    return data_result


# tambahan fitur bonus
# def random():
