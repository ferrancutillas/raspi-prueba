frase = input("Introduce una frase: ")

palabras = frase.split()

contador = 0
for palabra in palabras:
    for letra in palabra:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            contador += 1

print(f"La frase contiene {contador} vocales")