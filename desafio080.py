ordem = numeros = []
#numeros = [12, 2, 4, 10, 45]
for i in range(0,5):
    numeros.append(int(input("Digite um número: ")))
        #Se o número digitado é maior que o digitado anteriormente
    print(f"Números digitados: {numeros}")
    if len(numeros) > 1 and numeros[i] > numeros[i-1]: #Se a lista contém mais de um número e o número atual é maior do que o número anterior
    print("Sim")
    
    """if len(numeros) != 0: #Se a lista números não estiver vazia
        a = max(numeros) #Encontre o maior número
        ordem.append(a) #Adicione-o na lista ordem
        if a in numeros: #Se o maior número estiver na lista numeros
            numeros.remove(a) #Remova-o
            print(f"Restaram: {numeros}") #Mostre os números que restaram
    elif len(numeros) == 0: #Se a lista numeros ficar vazia
        print(f"Lista ordenada: ", end="")
        for o in ordem: #Me mostre a lista ordem
            print(f"{o}", end=" ")
        break"""