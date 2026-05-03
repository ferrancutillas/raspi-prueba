def calcular_precio(precio, iva =21):
    return precio + (precio * iva / 100)

opcion = input("¿Desea ajustar el precio del IVA? (s/n): ")
match opcion:
    case "s":
        precio, iva = map(float, input("Ingrese un precio y un iva separados por espacio: ").split())
        precio_final = calcular_precio(precio, iva)
    case "n":
        precio = float(input("Ingrese un precio: "))
        precio_final = calcular_precio(precio)

print(f"El precio final con IVA es : ${precio_final:.2f}")