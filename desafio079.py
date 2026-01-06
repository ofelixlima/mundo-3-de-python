valores = ordem = []
i = 0
c = ""
while True:
    append.valores(str(input("Digite um número: ").strip()[i])
    while not valores[i].isnumeric:
        append.valores(str(input("Valor inválido! Digite um número: ").strip()[i])
    valores[i] = int(valores[i])
    while valores[i] in valores[i]: #nao repete  valor inserido dentro da lista 
        del(valores[i])
    
    c = str(input("Você quer adicionar mais algum número? [S/N]: ")).strip().upper()[0]
    while c not in "NS":
        c = str(input("Você quer adicionar mais algum número? [S/N]: ")).strip().upper()[0]
    while "NS" in c:
        if "N" in c:
            break
    i += 1
print(f"Você digitou os números: ", end=" ")
for v in valores:
    print(v, end=" ")
ordem = valores.sort()
print(f"\nOrdem crescente dos números: ", end=" ")
for o in ordem:
    print(o, end=" ")
print("Programa encerrado")