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


# print(main_data.current_role, main_data.current_user)


def game():
    current_role = main_data.current_role
    while (True):
        x = input()
        if x == "HELP":
            command_help(current_role)
        elif x == "Login":
            print("Login gagal!")
            print(
                'Anda telah login dengan username {}, silahkan lakukan "logout" sebelum melakukan login kembali'.format(main_data.current_user))
        elif x == "Summon Jin":
            if (current_role == "bandung_bondowoso"):
                summon_jin()
            else:
                unauthorized()
        elif x == "Hilangkan Jin":
            if (current_role == "bandung_bondowoso"):
                hilangkan_jin()
            else:
                unauthorized()
        elif x == "Ubah Tipe Jin":
            if (current_role == "bandung_bondowoso"):
                ubah_tipe_jin()
            else:
                unauthorized()
        elif x == "Bangun":
            if (current_role == "jin_pembangun"):
                jin_bangun()
            else:
                unauthorized()
        elif x == "Kumpul":
            if (current_role == "jin_pengumpul"):
                jin_kumpul
            else:
                unauthorized()
        elif x == "Batch Kumpul":
            if (current_role == "bandung_bondowoso"):
                batch_kumpul()
            else:
                unauthorized()
        elif x == "Batch Bangun":
            if (current_role == "bandung_bondowoso"):
                batch_bangun()
            else:
                unauthorized()
        elif x == "Laporan Jin":
            if (current_role == "bandung_bondowoso"):
                laporan_jin()
            else:
                unauthorized()
        elif x == "Laporan Candi":
            if (current_role == "bandung_bondowoso"):
                laporan_candi()
            else:
                unauthorized()
        elif x == "Hancurkan Candi":
            if (current_role == "roro_jonggrang"):
                hancurkan_candi()
            else:
                unauthorized()
        elif x == "Ayam Berkokok":
            if (current_role == "roro_jonggrang"):
                ayam_berkokok()
            else:
                unauthorized()
        elif x == "Save":
            if (current_role == "roro_jonggrang" or current_role == "roro_jonggrang"):
                save()
            else:
                unauthorized()
        elif x == "Exit":
            exit()
        elif x == "logout":
            main_data.current_role = None
            main_data.current_user = None
            main_data.is_login = False
        else:
            notvalid()
