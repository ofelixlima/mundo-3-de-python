n = []
continuar = ""
while True:
    n.append(int(input("Digite um número: ")))
    t = len(n) - 1
    continuar = str(input("Quer continuar? [S/N]: ").strip().upper()[0])
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ").strip().upper()[0])
    if continuar in "N":
        print(f"Números digitados: {len(n)}")
        print(f"Lista de valores em ordem decrescente: {sorted(n, reverse=True)}")
        for i, j in enumerate(n):
            if j == 5:
                print(f"O número 5 está na posição {i}")
        break