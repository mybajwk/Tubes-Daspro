
import main_data
from builtin_function import csv_reader
#  read csv ()


def read_file():
    print("load user.csv ....")
    file = open(main_data.folder+"/user.csv", 'r')
    main_data.data_csv_user, main_data.user_len = csv_reader(file, ";")
    print("load candi.csv ....")
    file = open(main_data.folder+"/candi.csv", 'r')
    main_data.data_csv_candi, main_data.candi_len = csv_reader(file, ";")
    print(main_data.data_csv_candi)
    print("load bahan_bangunan.csv ....")
    file = open(main_data.folder+"/bahan_bangunan.csv", 'r')
    main_data.data_csv_bahan, main_data.bahan_len = csv_reader(file, ";")

    print("\nload data sukses... ")
