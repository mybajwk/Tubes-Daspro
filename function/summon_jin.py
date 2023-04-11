import main_data
import builtin_function


def cekuser(name):
    data = main_data.data_csv_user
    for i in range(1, main_data.user_len):
        if data[i][0] == name:
            return False
    return True


def summon_jin():
    print("Jenis jin yang dapat dipanggil:")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")
    opsi = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
    while (opsi != "1" and opsi != "2"):
        print('Tidak ada jenis jin bernomor "{}" !'.format(opsi))
        opsi = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
    role = None
    if opsi == "1":
        print('Memilih jin "Pengumpul".')
        role = "jin_pengumpul"
    else:
        print('Memilih jin "Pembangun"')
        role = "jin_pembangun"
    username = input("Masukkan username jin: ")
    while not (cekuser(username)):
        print('Username "{}" sudah diambil!'.format(username))
        username = input("Masukkan username jin: ")
    password = input("Masukkan password jin: ")
    len_password = builtin_function.len_data(password)
    while (len_password < 5 or len_password > 25):
        print("Password panjangnya harus 5-25 karakter!")
        password = input("Masukkan password jin: ")
        len_password = builtin_function.len_data(password)
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...\n")

    # insert data to variabel
    main_data.user_data[0] = username
    main_data.user_data[1] = password
    main_data.user_data[2] = role

    # insert to array
    main_data.data_csv_user = builtin_function.push_back_data(
        main_data.data_csv_user, main_data.user_data)

    print("Jin {} berhasil dipanggil!".format(username))
