from random import randint
from time import sleep
randint(1,60)
print(f"{'-'*50}")
print(f"{"JOGA NA MEGA SENA":^50}")
print(f"{'-'*50}")
q = 3 #int(input("Quantos jogos você quer que eu sorteie? ")) #3 [[6 numeros], [6 numeros], [6 numeros]]
print(f"{f" SORTEANDO {q} JOGOS ":=^50}") 
t = [[] for i in range(0,q)]
n = []
p = 0
limbo = 0
#[[6 numeros diferentes]]
for i in range(0,q): #Números
    for j in range(0,6): #Lista interna
        p = len(t[i])
        t[i].append(randint(1,60))
        #print(t[i]) #lista de números
        #print("t[i][j]: ",t[i][j])
        #print("t[i][j::-1]: ",t[i][j::-1]) #Cada número
        while p > 0:
            while t[i][p] < t[i][p-1]: #Se tamanho da lista maior que zero na contagem e numero atual igual ao um numero anterior
                print(t[i], end=" ")
                print(f"{t[i][p]} é menor que {t[i][p-1]}. Reordenando...")
                sleep(2)
                limbo = t[i][p]
                t[i][p] = t[i][p-1]
                t[i][p-1] = limbo
            if t[i][p] == t[i][p-1]: #Se último num é igual a num da lista
                print(f"{t[i][p]} já está na lista. Apagando e adicionando novo número na posição...")
                print(t[i])
                sleep(2)
                t[i][p] = randint(1,60)
                while t[i][p] < t[i][p-1]: #Se tamanho da lista maior que zero na contagem e numero atual igual ao um numero anterior
                    print(t[i], end=" ")
                    print(f"{t[i][p]} é menor que {t[i][p-1]}. Reordenando...")
                    sleep(2)
                    limbo = t[i][p]
                    t[i][p] = t[i][p-1]
                    t[i][p-1] = limbo
            p = p - 1
    n.append(t[i])
t.clear()
print(t)
print(n)
"""
n = [] #números varios
for i in range(0,5): #contagem até 5
    n.append(int(input("Digite um número: "))) #adiciona número em n
    p = len(n)-1 #quantidade de valores em n
    while p > 0 and n[p] < n[p-1]: #se a quantidade de n é maior que zero e o numero atual é menor que o anterior 
        temp = n[p] #manda o numero atual para um limbo temporário
        n[p] = n[p-1] #manda o numero anterior para o banquinho do atual
        n[p-1] = temp #manda o numero que tá no limbo para banquinho do anterior
        print(f"{n[p]} adicionado na posição {p}.") 
        print(f"{n[p-1]} adicionado na posição {p-1}.")
        p = p - 1 #diminua o tamanho por 1 a cada repetição while
    print(f"Números em ordem crescente: {n}")
"""