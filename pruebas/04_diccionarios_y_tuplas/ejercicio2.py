productos = {
    "manzana": 0.5,
    "banana": 0.3,
    "naranja": 0.7,
}

seleccion = input("Ingrese el nombre de los productos separados por espacios: ").split()

total = 0

for producto in seleccion:
    if producto in productos:
        total += productos[producto]
    else:
        print(f"El producto '{producto}' no está disponible.")
    
print(f"El total a pagar es: ${total:.2f}")