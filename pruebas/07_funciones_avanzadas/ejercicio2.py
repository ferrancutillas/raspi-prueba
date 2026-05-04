es_mayor_de_edad = lambda edad: edad >= 18

edad_usuario = int(input("Introduce tu edad: "))

if es_mayor_de_edad(edad_usuario):
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")

sumar = lambda a, b: a + b

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

resultado = sumar(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado}")