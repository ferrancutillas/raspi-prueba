# Ejercicio 1
for i in range(100, 201):
    if i % 5 == 0:
        print(i)

# Ejercicio 2
n = int(input("Introduce un número: "))

sumatorio = 0
for i in range(1, n+1):
    sumatorio = sumatorio + i
print(sumatorio)

# Ejercicio 3
sumatorio = 1
for i in range(1, n+1):
    sumatorio = sumatorio * i
print(sumatorio)

# Ejercicio 4
contador = 0
sumi = 0
coni = 0
mayp = 0
while True:
    num = int(input("Introduce un número: "))

    if num < 0 :
            break
    
    if num % 2 == 0 and num > mayp:
        mayp = num

    if num % 2 != 0:
        sumi = sumi + num
        coni = coni + 1

    contador += 1

medi = sumi/coni
print(f"La media de los impares es {medi}")
print(f"El número más grande de los pares es {mayp}")
print(f"Has introducido {contador} números")

# Ejercicio 5
sump = 0
contn = 0
menor = 0
while True:
    num = int(input("Introduce un número: "))

    if num == 0:
        break

    if num > 0:
        sump += num

    if num < 0:
        contn += 1

    if num < menor:
        menor = num

print(f"El sumatorio de los positivos es {sump}")
print(f"La cantidad de negativos ha sido {contn}")
print(f"El menor número ha sido {menor}")