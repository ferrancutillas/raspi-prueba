opcion = "s"

while opcion == "s":
    x = int(input("Introduce el primer número: "))
    y = int(input("Introduce el segundo número: "))

    print("El resultado de la sumas es: " + str(x+y))

    opcion = input("¿Quieres realizar otra suma? (s/n): ")
    while opcion != "s" and opcion != "n":
        opcion = input("Opción no válida. ¿Quieres realizar otra suma? (s/n): ")

print("¡Hasta luego!")