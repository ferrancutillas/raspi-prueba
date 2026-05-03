def saludar(nombre, idioma):
    if idioma == "es":
        return f"Hola, {nombre}"
    elif idioma == "en":
        return f"Hello, {nombre}"
    
nombre, idioma = input("Ingrese su nombre y su idioma (es/en) separados por espacio: ").split()

print(saludar(nombre, idioma))