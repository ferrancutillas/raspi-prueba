class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es ", self.nombre, " y tengo ", self.edad, " años.")
        
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        print("Estoy estudiando ", self.carrera)

    def __str__(self):
        return f"Estudiante(nombre={self.nombre}, edad={self.edad}, carrera={self.carrera})"

def crear_estudiante():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    carrera = input("Ingrese su carrera:")
    return Estudiante(nombre, edad, carrera)

lista = []
opcion = 0
while opcion != 3:
    try:
        print("1 - Crear estudiante")
        print("2 - Borrar estudiante")
        print("3 - Salir")
        opcion = int(input("Seleccione una opción:"))
        match opcion:
            case 1:
                estudiante = crear_estudiante()
                lista.append(estudiante)
                print("Estudiante creado exitosamente.")
            case 2:
                    print("Estudiantes actuales:")
                    for estudiante in lista:
                        print(estudiante)
                    
                    input_nombre = input("Ingrese el nombre del estudiante a borrar: ")
                    for estudiante in lista:
                        if estudiante.nombre == input_nombre:
                            lista.remove(estudiante)
                            print(f"Estudiante {input_nombre} eliminado.")
                            break
                    else:
                        print(f"No se encontró un estudiante con el nombre {input_nombre}.\n")
            case 3:
                print("Saliendo del programa...")
    except ValueError:
        print("Por favor, ingrese un número válido para la edad.\n")

for estudiante in lista:
    print(estudiante)

for estudiante in lista:
    estudiante.saludar()
    estudiante.estudiar()