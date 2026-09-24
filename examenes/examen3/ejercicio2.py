import random

filas = 6
columnas = 10

matriz = [[0]*columnas for _ in range(filas)]

for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = random.randint(1, 1000)
    print(matriz[i])

mayor = matriz[0][0]
menor = matriz[0][0]
ma_coordi= 0
ma_coordj = 0
me_coordi = 0
me_coordj = 0
for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            ma_coordi = i
            ma_coordj = j
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            me_coordi = i
            me_coordj = j
print(f"El valor máximo de la matriz es {mayor} y se encuentra en [{ma_coordi}][{ma_coordj}]")
print(f"El valor mínimo de la matriz es {menor} y se encuentra en [{me_coordi}][{me_coordj}]")
