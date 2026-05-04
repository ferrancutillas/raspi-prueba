def generar_numeros():
    lista= []
    contador= 0
    for i in range(1, 101):
        lista.append(i)
        contador += 1
        if contador == 10:
            print(f"{(i/10):.0f}º Tirada de numeros")
            yield lista
            contador = 0
            lista = []

for tirada in generar_numeros():
    print(tirada)