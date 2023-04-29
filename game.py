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


def game(x):
    current_role = main_data.current_role
    if x == "help":
        command_help(current_role)
    elif x == "login":
        print("Login gagal!")
        print(
            'Anda telah login dengan username {}, silahkan lakukan "logout" sebelum melakukan login kembali'.format(main_data.current_user))
    elif x == "summon jin" or x == "summonjin":
        if (current_role == "bandung_bondowoso"):
            if main_data.user_len <= 102:
                summon_jin()
            else:
                print(
                    "Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        else:
            unauthorized()
    elif x == "hilangkan jin" or x == "hilangkanjin":
        if (current_role == "bandung_bondowoso"):
            hilangkan_jin()
        else:
            unauthorized()
    elif x == "ubah tipe jin" or x == "ubahtipejin":
        if (current_role == "bandung_bondowoso"):
            ubah_tipe_jin()
        else:
            unauthorized()
    elif x == "bangun" or x == "jinbangun":
        if (current_role == "jin_pembangun"):
            jin_bangun()
        else:
            unauthorized()
    elif x == "kumpul" or x == "jinkumpul":
        if (current_role == "jin_pengumpul"):
            jin_kumpul()
        else:
            unauthorized()
    elif x == "batch kumpul" or x == "batchkumpul":
        if (current_role == "bandung_bondowoso"):
            batch_kumpul()
        else:
            unauthorized()
    elif x == "batch bangun" or x == "batchbangun":
        if (current_role == "bandung_bondowoso"):
            batch_bangun()
        else:
            unauthorized()
    elif x == "laporan jin" or x == " laporanjin":
        if (current_role == "bandung_bondowoso"):
            laporan_jin()
        else:
            unauthorized()
    elif x == "laporan candi" or x == "laporancandi":
        if (current_role == "bandung_bondowoso"):
            laporan_candi()
        else:
            unauthorized()
    elif x == "hancurkan candi" or x == "hancurkancandi":
        if (current_role == "roro_jonggrang"):
            hancurkan_candi()
        else:
            unauthorized()
    elif x == "ayam berkokok" or x == "ayamberkokok":
        if (current_role == "roro_jonggrang"):
            ayam_berkokok()
        else:
            unauthorized()
    elif x == "save":
        save()
    elif x == "exit":
        exit()
    elif x == "logout":
        logout()
    else:
        notvalid()
