import main_data
from help import command_help
from builtin_function import unauthorized, notvalid
from function.ayam_berkokok import ayam_berkokok
from function.batch import batch_bangun, batch_kumpul
from function.exit import exit
from function.hancurkan_candi import hancurkan_candi
from function.hilangkan_jin import hilangkan_jin
from function.jin_bangun import jin_bangun
from function.jin_kumpul import jin_kumpul
from function.laporan_candi import laporan_candi
from function.laporan_jin import laporan_jin
from function.save import save
from function.summon_jin import summon_jin
from function.ubah_tipe_jin import ubah_tipe_jin
from function.logout import logout


# print(main_data.current_role, main_data.current_user)


def game(command):
    # melakukan penegcekan command yang dikirim dan mengeck apakah role saat ini memiliki akses atau tidak
    current_role = main_data.current_role
    if command == "help":
        command_help(current_role)
    elif command == "login":
        print("Login gagal!")
        print(
            'Anda telah login dengan username {}, silahkan lakukan "logout" sebelum melakukan login kembali'.format(main_data.current_user))
    elif command == "summon jin" or command == "summonjin":
        if (current_role == "bandung_bondowoso"):
            if main_data.user_len <= 102:
                summon_jin()
            else:
                print(
                    "Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        else:
            unauthorized(current_role)
    elif command == "hilangkan jin" or command == "hilangkanjin":
        if (current_role == "bandung_bondowoso"):
            hilangkan_jin()
        else:
            unauthorized(current_role)
    elif command == "ubah tipe jin" or command == "ubahtipejin":
        if (current_role == "bandung_bondowoso"):
            ubah_tipe_jin()
        else:
            unauthorized(current_role)
    elif command == "bangun" or command == "jinbangun":
        if (current_role == "jin_pembangun"):
            jin_bangun()
        else:
            unauthorized(current_role)
    elif command == "kumpul" or command == "jinkumpul":
        if (current_role == "jin_pengumpul"):
            jin_kumpul()
        else:
            unauthorized(current_role)
    elif command == "batch kumpul" or command == "batchkumpul":
        if (current_role == "bandung_bondowoso"):
            batch_kumpul()
        else:
            unauthorized(current_role)
    elif command == "batch bangun" or command == "batchbangun":
        if (current_role == "bandung_bondowoso"):
            batch_bangun()
        else:
            unauthorized(current_role)
    elif command == "laporan jin" or command == " laporanjin":
        if (current_role == "bandung_bondowoso"):
            laporan_jin()
        else:
            unauthorized(current_role)
    elif command == "laporan candi" or command == "laporancandi":
        if (current_role == "bandung_bondowoso"):
            laporan_candi()
        else:
            unauthorized(current_role)
    elif command == "hancurkan candi" or command == "hancurkancandi":
        if (current_role == "roro_jonggrang"):
            hancurkan_candi()
        else:
            unauthorized(current_role)
    elif command == "ayam berkokok" or command == "ayamberkokok":
        if (current_role == "roro_jonggrang"):
            ayam_berkokok()
        else:
            unauthorized(current_role)
    elif command == "save":
        save()
    elif command == "exit":
        exit()
    elif command == "logout":
        logout()
    else:
        notvalid()
