def voto():
    from datetime import datetime
    ano = int(input("Em que ano você nasceu? \033[0;32m"))
    print('\033[m', end='')
    idade = datetime.now().year - ano
    if idade < 18:
        v = f'Com {idade} anos: NÃO VOTA.'
    elif idade >= 18 and idade <= 65:
        v = f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade > 65:
        v = f'Com {idade} anos: VOTO OPCIONAL.'
    return v
print(voto())
