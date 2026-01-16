from datetime import date
pessoa = {}
pessoa["Nome"] = str(input("Nome: ")).strip().capitalize() #Ana
pessoa["Ano de nascimento"] = int(input("Ano de Nascimento: ")) #1967
pessoa["CTPS"] = int(input("Carteira de Trabalho (Digite 0 se não tiver): "))
if pessoa["CTPS"] != 0:
    pessoa['Ano de contratação'] = int(input("Ano de contratação: ")) #1987
    pessoa['Salário'] = float(input("Salário: R$")) #1985.67
    pessoa["Idade"] = date.today().year - pessoa["Ano de nascimento"] #59
    print("-="*50)
    if pessoa["Ano de contratação"] + 35 >= 35:
        pessoa["Aposentadoria"] = (pessoa["Ano de contratação"] + 35) - pessoa["Ano de nascimento"] #55
else:
    pessoa['Idade'] = date.today().year - pessoa["Ano de nascimento"]
for d, v in pessoa.items():
    print(f"{d} tem o valor de {v}.")