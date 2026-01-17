jogador = {}
jogador['nome'] = str(input("Digite o nome do jogador: ")).strip().capitalize()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
for p in range(0,jogador['partidas']):
    jogador['gols'].append(int(input(f"Quantos gols {jogador['nome']} fez na partida {p}? ")))
del jogador["partidas"]
jogador['total'] = sum(jogador["gols"])
print("-="*25)
print(jogador)
print("-="*25)
for d, v in jogador.items():
    print(f"O campo {d} tem o valor {v}.")
print("-="*25)
print(f"O jogador {jogador['nome']} jogou {len(jogador["gols"])} partidas.")
for i in range(0,len(jogador['gols'])):
    print(f"  ==> Na partida {i}, fez {jogador["gols"][i]} gols.")
print(f"Foi um total de {jogador["total"]} gols.")