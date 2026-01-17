continuar = ''
pessoa = {}
grupo = []
while True:
    pessoa["nome"] = str(input("Nome: ")).strip().capitalize()
    pessoa["sexo"] = str(input("Sexo: ")).strip().upper()[0]
    while pessoa["sexo"] not in "MF" or isinstance(pessoa["sexo"], (float, int)):
        print("Sexo inválido! Digite de novo, por gentileza.")
        pessoa["sexo"] = str(input("Sexo: ")).strip().upper()[0]
    pessoa["idade"] = int(input("Idade: "))
    grupo.append(pessoa.copy())
    pessoa.clear()
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "NS":
        print("Dígito inválido! Tente de novo.")
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if continuar in "N":
        break

#grupo = [{'nome': 'Marcos', 'sexo': 'M', 'idade': 23}, {'nome': 'Laura', 'sexo': 'F', 'idade': 45}, {'nome': 'Lucas', 'sexo': 'M', 'idade': 21}, {'nome': 'Maria', 'sexo': 'F', 'idade': 57}, {'nome': 'Luis', 'sexo': 'M', 'idade': 30},{'nome': 'Mara', 'sexo': 'F', 'idade': 36}]

print("-="*25)
print(f"— O grupo tem {len(grupo)} pessoas.")
idades = [m["idade"] for m in grupo]
media = sum(idades) / len(idades)
print(f"— A média de idade é de {media:.1f}.")
feminino = [f for f in grupo if f["sexo"] in "F"]
print(f"— As mulheres cadastradas foram ", end="")
for c in feminino:
    for v in c.values():
        if isinstance(v, str) and v > v[0]:
            print(v, end=" ")
print()
upMedia = [a for a in grupo if a['idade'] > media]
print(f"— Lista de pessoas acima da média:")
for c in range(0,len(upMedia)):
    for d,v in upMedia[c].items():
        print(f"{d} = {v};", end=" ")
    print()
print("<< ENCERRADO >>")