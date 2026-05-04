def crear_usuario(**kwargs):
    usuario = {
        "nombre": kwargs.get("nombre", None),
        "edad": kwargs.get("edad", None),
        "email": kwargs.get("email", None),
        "pais": kwargs.get("pais", None)
    }
    return usuario

usuario = crear_usuario(nombre="Ferran", edad=30)
usuario2 = crear_usuario(nombre="Ana", email="ana@example.com", pais="España")

usuarios = [usuario, usuario2]

for u in usuarios:
    print(u)