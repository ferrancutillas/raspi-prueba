class StockError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

detalles = {
    101 : ("manzanilla", "infusiones"),
    102 : ("menta", "infusiones"),
    103 : ("capuchino", "cafe"),
    104 : ("latte", "cafe"),
}

stock = {
    101 : 200,
    102 : 150,
    103 : 100,
    104 : 50,
}

def actualizar_stock(id, cantidad):
    try:
        if stock[id] + cantidad < 0:
            raise StockError("El stock no puede ser negativo.")
        else:
            stock[id] += cantidad
            print(f"Stock actualizado para {detalles[id][0]}: {stock[id]}")
    except KeyError as ke:
        print(f"Error: El producto con ID {ke} no ha sido encontrado")

def mostrar_productos(id):
    try:
        print(f"Producto: {detalles[id][0]}, Categoría: {detalles[id][1]}, Stock: {stock[id]}")
    except KeyError as ke:
        print(f"Error: El producto con ID {ke} no ha sido encontrado")


id = int(input("Ingrese el ID del producto: "))
cantidad = int(input("Ingrese la cantidad a añadir o retirar: "))
try:
    actualizar_stock(id, cantidad)
except StockError as se:
    print(f"Error: {se.mensaje}")


id = int(input("Ingrese el ID del producto a mostrar: "))
mostrar_productos(id)
