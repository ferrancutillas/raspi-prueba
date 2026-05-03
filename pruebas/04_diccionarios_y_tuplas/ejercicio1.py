traductor = {
    "perro" : "dog",
    "gato" : "cat",
    "casa" : "house",
    "árbol" : "tree",
}

palabra = input("Introduce una palabra en espaol: ")

for clave, valor in traductor.items():
    if clave == palabra:
        print(f"La traducción de {palabra} es {valor}")