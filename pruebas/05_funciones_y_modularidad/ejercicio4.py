import math

def calcular_aea(figura):
    match figura:
        case "cuadrado":
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = lado ** 2
        case "rectangulo":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = base * altura
        case "triángulo":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = (base * altura) / 2
        case "círculo":
            radio = float(input("Ingrese el radio del círculo: "))
            area = math.pi * radio**2
        case _:
            print("Figura no reconocida.")
            return None
    return area

figura = input("Ingrese la figura (cuadrado, rectangulo, triángulo, círculo): ")
area = calcular_aea(figura)
if area is not None:
    print(f"El área de la {figura} es: {area:.2f}")
