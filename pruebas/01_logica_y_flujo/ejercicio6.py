lado1 = int(input("Introduce el primer lado del triángulo: "))
lado2 = int(input("Introduce el segundo lado del triángulo: "))
lado3 = int(input("Introduce el tercer lado del triángulo: "))

if lado1 == lado2 and lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 and lado1 != lado3 or lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado2 != lado1:
    print("el triángulo es isósceles")
else:
    print("El triángulo es escaleno")