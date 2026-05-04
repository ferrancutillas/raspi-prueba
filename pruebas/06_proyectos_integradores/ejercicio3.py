conversiones = {
    "USD" : 1.08,
    "GBP" : 0.85,
    "JPY" : 164.20,
}

def convertir_moneda(cantidad, moneda):
    try:
        cantidad_final = cantidad * conversiones[moneda]
        print(f"{cantidad} EUR son {cantidad_final:.2f} {moneda}")
    except KeyError as ke:
        print(f"Error: La moneda {ke} no es válida")
    
while True:
    try:
        cantidad = float(input("Ingrese la cantidad de euros a convertir: "))
        break
    except ValueError as ve:
        print(f"Error: La cantidad ingresada no es válida. Detalles: {ve}")

moneda = input("Ingrese la moneda a la que desea convertir (USD, GBP, JPY): ")

convertir_moneda(cantidad, moneda)