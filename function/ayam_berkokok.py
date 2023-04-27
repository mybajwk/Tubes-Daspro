import main_data


def ayam_berkokok():
    print("Kukuruyuk.. Kukuruyuk..")
    jumlah_candi = main_data.candi_len-1
    print("Jumlah Candi: ", jumlah_candi)
    if jumlah_candi >= 100:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    exit()
