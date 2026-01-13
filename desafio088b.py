n = [11, 20, 51, 25, 39, 40]
print(max(n))
print(n.index(max(n)))
if n[n.index(max(n))] > n[p]:
    print(f"{max(n)} não está na última posição.")
    temp = n[n.index(max(n))]
    del n[n.index(max(n))]
    n.append(temp)
print(n)
