import main_data


def login():
    data_user = main_data.data_csv_user
    username = input("masukkan username ")
    password = input("masukkan password ")
    idx = 0  # for indexing
    for i in data_user:
        if idx != 0:
            if i[0] == username:
                if i[1] == password:
                    print("selamat datang", username)
                    print(
                        "silahkan ketik `help` untuk daftar command yang dapat anda lakukan")
                    return username, i[2], True
                else:
                    print("password salah")
                    return None, None, False

        idx += 1
    print("username salah")
    return None, None, False
