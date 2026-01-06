valores = ordem = []
i = 0
c = ""
while True:
    valores.append(str(input("Digite um número: ").strip()))
    while not valores[i].isnumeric:
        valores.append(str(input("Valor inválido! Digite um número: ").strip()))
    if valores[i] in valores[:i]: #nao repete  valor inserido dentro da lista 
        valores.pop(i)
    valores[i] = int(valores[i])
    c = str(input("Você quer adicionar mais algum número? [S/N]: ")).strip().upper()[0]
    while c not in "NS":
        c = str(input("Você quer adicionar mais algum número? [S/N]: ")).strip().upper()[0]
    if "N" in c:
        break
    i += 1
print(f"Você digitou os números: ", end=" ")
for v in valores:
    print(v, end=" ")
ordem = sorted(valores, reverse=False)
print(f"\nOrdem crescente dos números: ", end=" ")
for o in ordem:
    print(o, end=" ")
print("\nPrograma encerrado")