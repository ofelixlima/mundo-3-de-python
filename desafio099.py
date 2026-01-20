from random import randint
from time import sleep
def separador():
    print("-="*15, flush=True)
def maior(* numeros, m = 0):
    separador()
    for n in numeros:
        if n > m:
            m = n
    for n in numeros:
        print(n, end=" ", flush=True)
        sleep(0.5)
    print("Fim", end=" ", flush=True)
    sleep(0.5)
    print(f"Foram gerados {len(numeros)} números.", flush=True)
    sleep(0.5)
    print(f"O maior número digitado foi {m}.", flush=True)
    separador()
def geradorNumeros(temp, contadores, todos):
    for f in contadores:    
        for g in range(f):
            g = randint(0, 10)
            g += 1
            temp = (*temp, g)
            sleep(0.5)
        if len(temp) == f:
            todos.append(temp)        
            temp = ()
    for i in todos:
        maior(*i)
geradorNumeros((),(6,3,2,1,0),[])