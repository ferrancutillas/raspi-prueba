class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return f"Vehículo {self.marca} de modelo {self.modelo}"

v1 = Vehiculo("Toyota", "Corolla")

print(v1)

class Coche(Vehiculo):
    def __init__(self, marca, modelo, combustible):
        super().__init__(marca, modelo)
        self.combustible = combustible

    def __str__(self):
        return super().__str__() + f"que funciona con {self.combustible}"
    
c1 = Coche("Honda", "Civic", "gasolina")
print(c1)

print(c1.__getattribute__("marca"))