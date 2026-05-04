precio_base = [100, 200, 300, 400, 500]
precio_iva = list(map(lambda x: x*1.21, precio_base))
print(precio_iva)

lenguajes = ["Python", "JavaScript", "Java", "C#", "Ruby", "Go", "Swift", "Kotlin", "PHP", "TypeScript"]
lenguajes_cortos = list(filter(lambda x: len(x)<=4, lenguajes))
print(lenguajes_cortos)
