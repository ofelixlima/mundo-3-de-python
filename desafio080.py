ordem = numeros = ant = atual = []
numeros = [12, 2, 4, 10, 45]
i = 0
while i < 5:
    print(f"numeros[{i}::-1]: {numeros[i::-1]}") #inverte
    i += 1

"""for i in range(0, 5):
    a = numeros.append(int(input("Digite um número: ")))
    b = numeros[:]
    print(f"Números digitados: {numeros}")
    print(f"i: {i}")
    print(f"b: {b}")
    if len(numeros) > 1:
        print(numeros)"""