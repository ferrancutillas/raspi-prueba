edad = int(input("Introduce tu edad: "))

if edad >= 65:
    print("Eres un anciano")
elif edad >= 18:
    print("Eres un adulto")
elif edad >= 13:
    print("Eres un adolescente")
else:
    print("Eres un niño")