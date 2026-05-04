with open ("/home/ferran/vscode/python/pruebas/09_herramientas_pythonicas/ejercicio3.txt", "a") as archivo:
    archivo.write("Esta es una nueva línea añadida a lo anterior\n")

with open ("/home/ferran/vscode/python/pruebas/09_herramientas_pythonicas/ejercicio3.txt", "r") as archivo:
    lineas = archivo.readlines()

with open ("/home/ferran/vscode/python/pruebas/09_herramientas_pythonicas/ejercicio3.txt", "w") as archivo:
    archivo.write("Esta línea sobreescribe lo anterior\n")

# Leemos el archivo linea por linea y eliminamos los espacios al principio y al final
for linea in lineas:
    print(linea.strip())