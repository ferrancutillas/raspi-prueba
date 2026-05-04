nombres = ["Ferran", "Jordi", "Pau", "Marta", "Anna"]
nombres2 = [len(nombre) for nombre in nombres]
nombres3 = {}

for i in range(len(nombres)):
    nombres3[nombres[i]] = nombres2[i]

print(nombres3)