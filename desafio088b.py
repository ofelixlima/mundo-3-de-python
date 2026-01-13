from random import randint
n = [2, 31, 45, 45, 53, 56]
for i in range(0,len(n)-1):
    p = len(n)-1
    while p > 0:
        while n[p] == n[p-1]:
            temp = n[p]
            n[p] = randint(1,60)
        p = p - 1
print(n)