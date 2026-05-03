saldo = 1000

print("Bienvenido al cajero automático")
opcion  = input("¿Qué operación desea realizar? (ingresar, retirar, consultar, salir): ")

match opcion:
    case "ingresar":
        saldo = saldo + int(input("¿cuánto dinero desea ingresar? "))
        print("Su saldo actual es: " +str(saldo))
    case "retirar":
        retirar = int(input("¿cuánto dinero desea retirar? "))
        if retirar > saldo:
            print("No tiene suficiente saldo para realizar la operación")
        else:
            saldo = saldo - retirar
    case "consultar":
        print("Su saldo actual es: " +str(saldo))
    case "salir":
        print("Gracias por usar el cajero automático, vuelva pronto")