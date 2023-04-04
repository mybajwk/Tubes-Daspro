import csv
import main_data
#  read csv ()


def read_file(file_name):
    file = open(main_data.folder+"/"+file_name+".csv", 'r')
    match file_name:
        case "user":
            main_data.data_csv_user = list(csv.reader(file, delimiter=";"))
        case "candi":
            main_data.data_csv_candi = list(csv.reader(file, delimiter=";"))
        case "bahan_bangunan":
            main_data.data_csv_bahan = list(csv.reader(file, delimiter=";"))
        case _:
            print("File tidak ada yang sesuai")
