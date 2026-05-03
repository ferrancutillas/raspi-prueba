filas = int(input("Introduce un nñumero de filas: "))

for i in range(1, filas +1):
    for j in range(1, i +1):
        print("*", end=" ")
    print()