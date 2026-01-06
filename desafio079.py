valores = []
i = 0
c = ""
ordem = []
While True:
    append.valores(int(input("Digite um número: "))
    while not valores[i].isnumeric:
        append.valores(int(input("Valor inválido! Por favor, digite um número: "))
    while valores[i] in valores[i]: #nao repete  valor inserido dentro da lista 
        del(valores[i])
    c = str(input("Você quer adicionar mais algum número? [S/N]: ")).strip().upper()[0]
    while c not in "NS":
        c = str(input("Você quer adicionar mais algum número? [S/N]: ")).strip().upper()[0]
    while "NS" in c:
        if "N" in c:
            break
print(f"Você digitou os números: ", end=" ")
for v in valores:
    print(v, end=" ")
ordem = valores.sort()
print(f"\nOrdem crescente dos números: ",)
for o in ordem:
    print(o, end=" ")
print("Programa encerrado")