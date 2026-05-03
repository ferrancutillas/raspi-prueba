numeros = []

for i in range (0, 3):
    x = int(input("ingrese un número: "))
    numeros.append(x)

numeros.pop(1)

print(numeros)