import random

def analizarArray(array, array2):
    for i in range(len(array)):
        if array[i] > 100:
            array2.append(array[i])
    return array2

numeros = []
for i in range(100):
    numeros.append(random.randint(1,200))
print(numeros)

numeros2= []
numeros2 = analizarArray(numeros, numeros2)
print(numeros2)

