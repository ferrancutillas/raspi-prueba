numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Por cada elemento si este es par obtenemos su cuadrado y lo metemos en una nueva lsita
numeros2 = [x**2 for x in numeros if x%2 == 0]

print(numeros2)

