import functools

productos =[
        {"nombre": "ratón", "precio": 25},
        {"nombre": "teclado", "precio": 45},
        {"nombre": "monitor", "precio": 150},
        {"nombre": "impresora", "precio": 120},
        {"nombre": "altavoces", "precio": 80}
]

productos_filtrados = list(filter(lambda x: x["precio"] > 50, productos))
precio_total = functools.reduce(lambda a, b: a + b, map(lambda x: x["precio"], productos_filtrados))
# formma simplificada
# precio_total = sum(map(lambda x: x["precio"], productos_filtrados))

print(productos_filtrados)
print(precio_total)