from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input("Dígite o ano que você nasceu: "))
idade = ano_atual - ano_nascimento
if idade >= 18:
    print(f"Você tem {idade} anos. Acesso permitido!")
else:
    print(f"Você tem {idade} anos. Acesso negado por ser menor de idade.")
