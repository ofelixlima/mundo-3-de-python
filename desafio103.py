def ficha(nome='<desconhecido>', gols=0):
    print('-'*25)
    n = str(input("Nome do jogador: ")).strip()
    if n in '': 
        n = nome    
    try:    
        g = int(input("Número de gols: "))
    except ValueError:
        g = gols
    out = print(f'O jogador {n} fez {g} gol(s) no campeonato.')
    return out
ficha() 