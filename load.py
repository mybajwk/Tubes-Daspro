import csv
import main_data
from builtin_function import csv_reader
#  read csv ()


def read_file(file_name):
    match file_name:
        case "user":
            file = open(main_data.folder+"/"+file_name+".csv", 'r')
            main_data.data_csv_user = csv_reader(file, ";")
        case "candi":
            file = open(main_data.folder+"/"+file_name+".csv", 'r')
            main_data.data_csv_candi = csv_reader(file, ";")
        case "bahan_bangunan":
            file = open(main_data.folder+"/"+file_name+".csv", 'r')
            main_data.data_csv_bahan = csv_reader(file, ";")
        case _:
            print("File tidak ada yang sesuai")
