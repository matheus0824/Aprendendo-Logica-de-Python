import math

def calcular_trigonometria():
    print("---Calculadora Trigonométrica---")
    print("Opções: [s] SENO, [c] COSSENO, [t]TANGENTE")

    operacao = input("Dígite a operação desejada: ").lower()
    angulo_g = float(input("Dígite o valor do ângulo em graus: "))

    angulo_r = math.radians(angulo_g)

    if operacao == "s":
        resultado = math.sin(angulo_r)
        print(f"O seno de {angulo_g}º é: {round(resultado, 4)}")

    elif operacao == "c":
        resultado = math.cos(angulo_r)
        print(f"O cosseno de {angulo_g}º é: {round(resultado, 4)}")

    elif operacao == "t":
        resultado = math.tan(angulo_r)
        print(f"A tangente de {angulo_g}º é: {round(resultado, 4)}")


    else:
        print("Operação inválida. Use 's', 'c' ou 't'.")


if __name__ == "__main__":
    calcular_trigonometria()