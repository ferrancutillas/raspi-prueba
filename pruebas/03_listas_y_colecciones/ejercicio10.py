matriz = [
    ["o", "o", "o"],
    ["o", "o", "o"],
    ["o", "o", "o"]
]

fila, columna = map(int, input("Introduce el numero de la fila y la columna (seprados por un espacio): ").split())

matriz[fila][columna] = "x"

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")  
    print()
