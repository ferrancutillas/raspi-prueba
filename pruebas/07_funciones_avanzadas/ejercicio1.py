def sumar_todos(lista):
    return sum(lista)

lista = input("Introduce una lista de números separados por espacios: ").split()
for numero in lista:
    try:
        float(numero)
        lista[lista.index(numero)] = float(numero) 
    except ValueError as ve:
        print(f"Error: '{numero}' no es un número válido. Detalles: {ve}")
        exit()

suma = sumar_todos(lista)
print(suma)