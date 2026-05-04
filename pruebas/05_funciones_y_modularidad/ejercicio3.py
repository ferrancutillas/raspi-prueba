def conversor_temperatura(cantidad, unidad = "C"):
   match unidad:
        case "C":
            cantidad = (cantidad - 32) * 5/9
            return f"La temperatura es {cantidad:.2f}°{unidad}"
        case "F":
            cantidad = (cantidad *9/5) + 32
            return f"La temperatura es {cantidad:.2f}°{unidad}"
        case _:
            return "Uidad no reconocida"

print(conversor_temperatura(100))
print(conversor_temperatura(212, "F"))
print(conversor_temperatura(50, "K"))