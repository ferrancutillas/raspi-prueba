notas = [8, 7, 9, 5, 10]
notas.sort(reverse=True)
print (notas)

suma = 0
contador = 0
for nota in notas:
    suma += nota
    contador += 1

promedio = suma / contador
print("El promedio de las notas es: " +str(promedio))

# Otra forma de calcular la media con funciones sería la siguiente:

suma2 = sum(notas)
cantidad = len(notas)

promedio2 = suma2 / cantidad
print("El promedio de las notas es: " +str(promedio2))