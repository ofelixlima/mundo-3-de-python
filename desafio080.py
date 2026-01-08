n = []
for i in range(0,5):
    n.append(int(input("Digite um número: ")))
    p = len(n)-1
    while p > 0 and n[p] < n[p-1]:
        temp = n[p]
        n[p] = n[p-1]
        n[p-1] = temp
        print(f"{n[p]} adicionado na posição {p}.")
        print(f"{n[p-1]} adicionado na posição {p-1}.")
        p = p -1
    print(f"Números em ordem crescente: {n}")