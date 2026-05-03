x = 1

for i in range(1, 11):
    print("Tabla del " +str(i) +": " )
    x = 1
    for j in range(i, i*10 +i, i):
        print(str(x) +" x " +str(i) +" = " +str(j))
        x += 1