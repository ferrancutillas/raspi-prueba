class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo 

    @property
    def saldo(self):
        return f"El saldo actual de {self.titular} es: {self.__saldo}"
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if self.__saldo + nuevo_saldo < 0:
            print("El saldo no puede ser negativo.")
        else:
            self.__saldo = self.__saldo + nuevo_saldo

c1 = CuentaBancaria("Juan", 1000)
opcion = input("¿Desea retirar o ingresar dinero? (r/i): ")

while True:
    match opcion:
        case "r":
            saldo = float(input("Ingrese el dinero que quiere retirar: "))
            break
        case "i":
            saldo = float(input("Ingrese el dinero que quiere ingresar: "))
            break
        case _:
            print("Opción no válida.")
c1.saldo = saldo

print(c1.saldo)