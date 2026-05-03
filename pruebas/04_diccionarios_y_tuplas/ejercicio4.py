coordenadas = (10, 20)

try:
    coordenadas.append(30)
except Exception as e:
    print(f"Error: {e}")

try:
    coordenadas[0] = 15
except Exception as e:
    print(f"Error: {e}")

x, y = coordenadas
print(f"Coordenadas: x={x}, y={y}")