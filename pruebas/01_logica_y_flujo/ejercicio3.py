precio = int(input("introduce el precio de la compra: "))
descuento = 0.85

if precio >= 100:
    precio_final = precio * descuento
else:
    precio_final = precio

print("El precio final de tu compra es " + str(precio_final))