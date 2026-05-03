nombres = ["Juan", "María", "Pedro", "Ana", "Luis"]

nombre = input("Introduce un nombre: ")

if nombre in nombres:
    print(f"{nombre} se encuentra en la lista.")
else:
    print(f"{nombre} no se encuentra en la lista.")