import csv
import main_data
#  read csv ()


def read_file(file_name):
    match file_name:
        case "user":
            file = open(main_data.folder+"/"+file_name+".csv", 'r')
            main_data.data_csv_user = list(csv.reader(file, delimiter=";"))
        case "candi":
            file = open(main_data.folder+"/"+file_name+".csv", 'r')
            main_data.data_csv_candi = list(csv.reader(file, delimiter=";"))
        case "bahan_bangunan":
            file = open(main_data.folder+"/"+file_name+".csv", 'r')
            main_data.data_csv_bahan = list(csv.reader(file, delimiter=";"))
        case _:
            print("File tidak ada yang sesuai")
