import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Solicitar coordenadas al usuario
def main():
    print("Calculadora de distancia entre dos puntos")
    x1 = float(input("Ingresa x1: "))
    y1 = float(input("Ingresa y1: "))
    x2 = float(input("Ingresa x2: "))
    y2 = float(input("Ingresa y2: "))
    distancia = calcular_distancia(x1, y1, x2, y2)
    print(f"La distancia entre los puntos es: {distancia}")

if __name__ == "__main__":
    main()
