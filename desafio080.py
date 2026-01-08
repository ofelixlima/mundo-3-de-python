n = [12, 14, 110, 21, 2, 56, 0, 78]
ultimo = anterior = []
for i in range(0,8):
    for j in range(0,8):
        #print(f"n[{i}], n[{j}]: {n[i], n[j]}")
        anterior = n[i]
        ultimo = n[j]
        if anterior == ultimo:
            anterior < ultimo
        elif len(n) > 1:
            if anterior > ultimo:
                temp = anterior
                n.remove(anterior)
                n.append(temp)
                del temp
            elif anterior < ultimo:
                temp = ultimo
                n.remove(ultimo)
                n.append(temp)
                del temp
        print(n)