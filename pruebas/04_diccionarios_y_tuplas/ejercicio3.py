contactos = {
    "Juan" : {"telefono" : "666666666", "email" : "juan@email.com"},
    "Maria" : {"telefono" : "777777777", "email" : "maria@email.com"},
    "Pedro" : {"telefono" : "888888888", "email" : "pedro@email.com"},
    "Ana" : {"telefono" : "999999999", "email" : "ana@email.com"}
}

print(f"Contactos disponibles: {list(contactos.keys())}")
personas = input("Selecciona a las personas separadas por espacios: ").split()

for persona in personas:
    for key in contactos:
        if key == persona:
            print(f"{key} - Teléfono {contactos[key]['telefono']} - Email {contactos[key]['email']}")
