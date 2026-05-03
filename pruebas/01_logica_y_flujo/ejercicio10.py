import random

numero_aleatorio = random.randint(1, 3)
maquina = ""

if numero_aleatorio == 1:
    maquina = "piedra"
elif numero_aleatorio == 2:
    maquina = "papel"
else:
    maquina = "tijeras"

usuario = input("Elije piedra, papel o tijeras: ")
opciones = ["piedra", "papel", "tijeras"]

if usuario == maquina:
    print("Empate, ambos eligieron " + usuario)
elif (usuario == "piedra" and maquina == "tijeras") or (usuario == "papel" and maquina == "piedra") or (usuario == "tijeras" and maquina == "papel"):
    print("Ganaste, la máquina eligió " +maquina)
else:
    if usuario not in opciones:
        print("Opción no válida, seleccione una de estas opciones " + str(opciones))
    else:
        print("Perdiste, la máquina eligió " +maquina)