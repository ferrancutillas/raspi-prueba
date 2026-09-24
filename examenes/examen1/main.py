# Ejercicio 1
nota1 = 5.67
nota2 = 4.33
nota3 = 8.56

media = (nota1 + nota2 + nota3)/3
media = round(media, 2)
print(f"La media de las 3 notas es {media}" )

# Ejercicio 2
numero = int(input("Introduce un número: "))
if numero % 5 == 0:
    print("El número introducido es mútiplo de 5")
if numero % 2 == 0:
    print("El número es par")

# Ejercicio 3
edad = int(input("Introduce tu edad: "))
if edad < 18 :
    falta = 18 - edad
    print(f"Te falta para ser mayor de edad {falta} año/s")
if edad >= 18 :
    sobra = edad - 18
    print(f"Llevas siendo mayor de edad {sobra} año/s")

# Ejercicio 4
precio = int(input("Introduce el precio del producto: "))
iva = input("Introduce el tipo de iva (general, reducido, superreducido): ")
codigo = input("Introduce tu código de descuento (nopro, mitad, meno5, 5porc): ")

if iva == "general" :
    precio = precio + ((precio*21)/100)
if iva == "reducido" :
    precio = precio + ((precio*10)/100)
if iva == "superreducido" :
    precio = precio + ((precio*4)/100)

if codigo == "nopro" :
    precio = precio
if codigo == "mitad" :
    precio = precio/2
if codigo == "meno5" :
    precio = precio - 5
if codigo == "5porc" :
    precio = precio - ((precio*5)/100)

precio = round(precio, 2)
print(f"El precio final es de {precio}")