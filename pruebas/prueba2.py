import random

def generar_numero_aleatorio():
    return random.randint(1, 100)

numero = generar_numero_aleatorio()
numero2 = 0

while numero2 != numero:
    numero2 = int(input("Adivina el número entre 1 y 100: "))
    if numero2 < numero:
        print("El número es mayor.")
    elif numero2 > numero:
        print("El número es menor.")
    else:
        print("¡Felicidades! Has adivinado el número.")