class NotaInvalidaError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def anyadir_nota(nombre, nota):
    if nota < 0 or nota > 10:
        raise NotaInvalidaError("La nota debe estar entre 0 y 10.")
    elif nombre in alumnos:
        alumnos[nombre].append(nota)
        print(f"Nota añadida para {nombre}.")
    else:
        print(f"El alumno {nombre} no existe en la lista.")
        alumnos[nombre] = [nota]
        print(f"Alumno {nombre} añadido con la nota {nota}.")

def obtener_promedio(nombre):
    try:
        notas = alumnos[nombre]
        promedio = sum(notas) / len (notas)
        return f"El promedio de {nombre} es: {promedio:.2f}"
    except KeyError as ke:
        return f"El alumno {ke} no existe en la lista."

alumnos = {
    "Juan" : [8, 9.3, 7.5],
    "María" : [9.5, 8.7, 9],
    "Pedro" : [7, 6.5, 8.2],
    "Ana" : [9, 9.2, 8.8]
}
    
opcion = 0
while opcion != 4:
    print("\nMenú:")
    print("1. Añadir nota a un alumno")
    print("2. Obtener promedio de un alumno")
    print("3. Mostrar alumnos y sus notas")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    while opcion < 1 or opcion > 4:
        opcion = int(input("Por favor, seleccione una opción válida (1-4): "))

    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del alumno: ")
            nota = float(input("Ingrese la nota a añadir: "))
            try:
                anyadir_nota(nombre, nota)
            except NotaInvalidaError as e:
                print(f"Error: {e.mensaje}")
        case 2:
            nombre = input("Ingrese el nombre del alumno: ")
            print(obtener_promedio(nombre))
        case 3:
            for alumno in alumnos:
                promedio = obtener_promedio(alumno)
                print(f"{alumno}: {alumnos[alumno]} - {promedio}")
        case 4:
            print("Saliendo del programa.")