numeros = []
for i in range(1, 21):
    numeros.append(i)

print(numeros)

numeros2 = []
for numero in numeros:
    if numero % 3 == 0:
        numeros2.append(numero)

print(numeros2)