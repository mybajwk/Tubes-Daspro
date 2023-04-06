seedInt = 2
x = seedInt
a = 3
c = 1
m = 19
for i in range(1, 11):
    LCG = ((a*x)+c) % m
    print(LCG)
    #print (x)
    x = x + 1
