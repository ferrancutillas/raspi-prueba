user_db = "admin"
password_db = "1234"

user_input = input("Introduce el usuario: ")
password_input = input("Introduce la contraseña: ")

if user_input != user_db:
    print("Usuario no encontrado")
elif password_input != password_db:
    print("Contraseña incorrecta")
else:
    print("Acceso concedido")