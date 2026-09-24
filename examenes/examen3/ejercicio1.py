matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

contador = 0
for i in range(3):
    for j in range(3):
        contador += 1
        matriz[i][j] = contador
    print(matriz[i])
print(f"\n")

matriz2 = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

contador = 0
for i in range(3):
    for j in range(3):
        contador += 1
        matriz2[i][j] = contador
    print(matriz2[i])
print(f"\n")

matriz3= [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(3):
    for j in range(3):
        matriz3[i][j]= matriz[i][j] + matriz2[i][j]
    print(matriz3[i])