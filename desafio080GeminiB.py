#Treino extra de Insertion Sort (ou Ordenação por Inserção)
nome = []
for i in range(0,5): #Faça esse pedido 5 vezes
    nome.append(str(input(f"Digite o {i+1}º nome: ").strip())) #Pede o nome
    p = len(nome) - 1 #resgata o tamano de nome - 1 (para não exceder o tamanho real)
    while p > 0 and nome[p] < nome[p-1]: #Enquanto o tamanho for maior que zero e o nome atual for maior que o anterior
        temp = nome[p] #Salve o nome temporariamente
        nome[p] = nome[p-1] #Troque o nome atual com o nome anterior
        nome[p-1] = temp #Carregue o nome salvo
        print(f"{nome[p]} adicionado na posição {p}.")
        print(f"{nome[p-1]} adicionado na posição {p-1}.")
        p = p - 1 #Mova a lista subtraindo por -1 em cada item
    print(f"Nomes em ordem alfabética: {nome}")