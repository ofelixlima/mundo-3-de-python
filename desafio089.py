from time import sleep
temp = []
notas = []
alunos = []
continuar = ""
while True:
    temp.append(str(input("Nome: ")).strip().capitalize())
    notas.append(int(input("Nota 1: ")))
    notas.append(int(input("Nota 2: ")))
    temp.append(notas[:])
    notas.clear()
    media = sum(temp[1])/len(temp[1])
    temp.append(media)
    del media
    alunos.append(temp[:])
    temp.clear()
    #print(alunos) #[['Marcos', [6, 9], 7.5], ['Felix', [7, 9], 8.0]]
    continuar = str(input("Quer adicionar mais um aluno? [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Quer adicionar mais um aluno? [S/N]: ")).strip().upper()[0]
    if continuar in "N":
        nome = [n[0] for n in alunos]
        notas = [p[1] for p in alunos]
        media = [m[2] for m in alunos]
        print("=-"*50)
        print(f"{"Nº":<6} {"NOME":<10} {"MÉDIA":<5}")
        print("-"*25)
        for i in range(0,len(nome)):
            print(f"{i:<6} {nome[i]:<10} {media[i]:<5}")
        print("-"*50)
        escolha = 0
        while escolha != 999:
            escolha = int(input("Deseja mostrar as notas de qual aluno? (999 interrompe): "))
            while escolha > len(alunos)-1 and escolha < 999:
                escolha = int(input("Quantidade inválida! Deseja mostrar as notas de qual aluno? (999 interrompe): "))
            if escolha == 999:
                break
            elif escolha != 999 and escolha <= len(alunos)-1:
                print(f"Notas de {nome[escolha]} são {notas[escolha]}.")
        break
print(f"FINALIZANDO...")
sleep(1)
print("<<< VOLTE SEMPRE >>>")