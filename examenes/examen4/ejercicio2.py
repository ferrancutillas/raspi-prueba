def buscarPalabra(palabra, array):
    contador = 0
    for i in range(len(array)):
        if palabra == array[i]:
            contador += 1
    return contador
    

palabras = []

for i in range(10):
    p = input("Introduce una palabra: ")
    palabras.append(p)
print(palabras)

buscar = input("Introduce una palabra a buscar: ")
contador = buscarPalabra(buscar, palabras)
print(f"La palabra {buscar} aparece {contador} veces")