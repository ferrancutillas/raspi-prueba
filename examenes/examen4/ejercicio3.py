notas = [7.5, 4.5, 8.8, 5.2, 9.1, 6.0, 7.8, 9.5, 3.0, 7.5, 8.1, 8.6, 9.2, 5.8, 4.2, 6.8, 4.5, 3.8]

def calcularPromedio(array):
    promedio = 0
    for i in range(len(array)):
        promedio = promedio + array[i]
    return promedio/len(array)

def contarAprobados(array):
    contador = 0
    for i in range(len(array)):
        if array[i] >= 5:
            contador += 1
    return contador

def encontrarNotaMaxima(array):
    nota = 0
    for i in range(len(array)):
        if array[i] > nota:
            nota = array[i]
    return nota

def mostrarNotas(array):
    print(array)

while True:
    opcion = int(input("1 - Calcular promedio\n2 - Contar aprobados\n3 - Nota máxima\n4 - Mostrar notas\n5 - Salir\nIntroduce una opción: "))
    match opcion:
        case 5:
            break
        case 1:
            promedio = calcularPromedio(notas)
            print(f"El promedio de las notas es {promedio}")
        case 2:
            aprobados = contarAprobados(notas)
            print(f"La cantidad de aprobados es: {aprobados}")
        case 3:
            nota = encontrarNotaMaxima(notas)
            print(f"La nota máxima es un {nota}")
        case 4:
            mostrarNotas(notas)