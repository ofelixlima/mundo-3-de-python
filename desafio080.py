numeros = []
for i in range(0, 5):
    numeros.append(int(input("Digite um número: "))) #Digita 5 números
    if len(numeros) == 1:
        numeros.append(int(input("Digite um número: ")))
    elif len(numeros) >= 2:
        a = numeros[i]
        b = numeros[i-1]
        if a > b:
            numeros.append(a)
        elif b > a:
            numeros.remove(b)
            numeros.insert(b, a)
        del(a,b)
    print(numeros)
