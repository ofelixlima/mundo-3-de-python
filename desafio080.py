n = tam = []
for i in range(0,5):
    n.append(int(input("Digite um número: ")))
    tam = len(n)
    p = len(n)-1
    while p > 0 and n[p] < n[p-1]:
        temp = n[p]
        n[p] = n[p-1]
        n[p-1] = temp
        p = p -1
    print(n)