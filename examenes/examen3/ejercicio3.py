import random

filas = 5
columnas = 12

matriz = [[0]*columnas for _ in range(filas)]

media = 0
contador = 0
contador2 = 0
for i in range(filas):
    media = 0
    for j in range(columnas):
        matriz[i][j]= random.randint(1, 2000)
        media = media + matriz[i][j]
    print(matriz[i])
    media = round(media/columnas, 2)
    print(f"La media del vendedor {i+1} es: {media} ventas")
    if media >= 1000:
        contador += 1
    else:
        contador2 += 1
print(f"{contador} vendedores superaron la media")
print(f"{contador2} vendedores no superaron la media")

media2 = 0
for i in range(columnas):
    media2 = 0
    for j in range(filas):
        media2 = media2 + matriz[j][i]
    media2 = round(media2/filas, 2)
    print(f"La media del mes {i+1} es {media2}")