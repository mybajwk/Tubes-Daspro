def adapadalist(a, list):
    for x in list:
        if x == a:
            return True
    return False


list = []
listtambah = []
a = 1
system = True
N = 0
while N != -9999:
    N = int(input())
    if N != -9999:
        list.append(N)
panjang = len(list)
print(list)
idx = 1
system = True
while (system):
    cek = True
    for x in range(panjang):
        for y in range(x+1, panjang):
            jumlah = list[x]+list[y]
            if jumlah == idx or idx == list[x] or idx == list[y]:
                cek = False
    if cek:
        print(idx)
        system = False
    idx += 1
# atas = max(list)
# bawah = min(list)

# while system == True:
#     if adapadalist(a, list):
#         pass
#     else:
#         if adapadalist(a, listtambah):
#             pass
#         else:
#             print(a)
#             system = False
#     a = a+1
