import main_data


def login():
    # melakukan login dan memberi return username, role, dan status is login
    data_user = main_data.data_csv_user
    username = input("masukkan username ")
    password = input("masukkan password ")
    for i in range(main_data.user_len):
        if data_user[i][0] == username:
            if data_user[i][1] == password:
                print("selamat datang", username)
                print(
                    'Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
                return username, data_user[i][2], True
            else:
                print("password salah")
                return "", "", False

    print("username salah")
    return "", "", False
