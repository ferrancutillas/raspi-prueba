anyo = int(input("Introduce un año: "))

if (anyo%4 == 0 and anyo%100 != 0) or (anyo%400 == 0):
    print("El año no es bisiesto")
else:
    print("El año es bisiesto")