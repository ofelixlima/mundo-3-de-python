from random import randint
from time import sleep
def final():
    print("FIM")
def divisor():
    print("-="*25)
start = [{"inicio": 1, "fim": 10, "passo": 1}, {"inicio": 10, "fim": 0, "passo": 2}]
def inicio():
    for s in range(len(start)):
        print(f"Contagem de {start[s]["inicio"]} até {start[s]["fim"]} de {start[s]["passo"]} em {start[s]["passo"]}:")    
        while start[s]["inicio"] >= start[s]["fim"]:
            print(start[s]['inicio'], end=" ", flush=True)
            start[s]['inicio'] -= start[s]['passo']
            sleep(0.25)
            if start[s]['inicio'] <= 0:
                break
        while start[s]['inicio'] <= start[s]['fim']:
            print(start[s]['inicio'], end=" ", flush=True)
            start[s]['inicio'] += start[s]['passo']
            sleep(0.25)
        final()
        divisor()
def contador(inicio, fim, passo):
    if passo <= 0:
        passo = 1
        print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}:")
    else:
        print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}:")
    while inicio != fim:
        if inicio <= fim:
            print(inicio, end=" ", flush=True)
            inicio =+ passo
        elif inicio >= fim:
            print(inicio, end=" ", flush=True)
            inicio -= passo
        elif passo == 0:
            if inicio > fim:
                inicio -= passo
            elif fim > inicio:
                inicio += passo
        sleep(0.25)
    print(inicio, end=" ", flush=True)
    final()
divisor()
inicio()
print("Agora é a sua vez de personalizar a contagem!")
contador(inicio = int(input("Início: ")), fim = int(input("Fim: ")), passo = int(input("Passo: ")))