def calcular_pendiente(x1, y1, x2, y2):
    if x2 == x1:
        raise ValueError("La pendiente es indefinida (división por cero, x1 = x2)")
    return (y2 - y1) / (x2 - x1)

# Opción 1: Puntos definidos en el código
punto1 = (1, 2)
punto2 = (4, 6)
try:
    pendiente = calcular_pendiente(punto1[0], punto1[1], punto2[0], punto2[1])
    print(f"Pendiente (puntos en código): {pendiente}")
except ValueError as e:
    print(e)

# Opción 2: Pidiendo los valores al usuario
try:
    x1 = float(input("Ingresa x1: "))
    y1 = float(input("Ingresa y1: "))
    x2 = float(input("Ingresa x2: "))
    y2 = float(input("Ingresa y2: "))
    pendiente_usuario = calcular_pendiente(x1, y1, x2, y2)
    print(f"Pendiente (valores ingresados): {pendiente_usuario}")
except ValueError as e:
    print(e)
