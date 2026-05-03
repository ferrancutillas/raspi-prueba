intentos = 0
pin = "1234"

while intentos < 3:
    pin_input = input("Introduce el PIN: ")
    if pin_input != pin:
        intentos += 1
        if intentos == 3:
            print("Has agotado tus intentos, saliendo del cajero... ")
    else:
        print("PIN correcto, accediendo a tu cuenta... ")
        break