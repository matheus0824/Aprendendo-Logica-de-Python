import math

def calcular():
    raio = float(input("Digite o valor do raio: "))

    perimetro = 2 * math.pi * raio
    area = math.pi * (raio **2)

    print(f"O perímetro é: {round(perimetro, 3)}")
    print(f"A area é: {round(area, 3)}")

if __name__ == "__main__":
    calcular()