from main_data import candi_data

def hancurkan_candi():
    id_candi = input("Masukkan ID candi: ")
    is_candi_ada = False 
    row = 0
    for i in range(100):
        if candi_data [i][0] == id_candi:
            is_candi_ada = True
            row = i
            break
    
    if is_candi_ada == True:
        konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")
        if konfirmasi == 'Y':
            candi_data[row][0] = ''
            candi_data[row][1] = ''
            candi_data[row][2] = ''
            candi_data[row][3] = ''
            candi_data[row][4] = ''

            print("\nCandi telah berhasil dihancurkan")
    else:
        print("Tidak ada candi dengan ID tersebut.")



   