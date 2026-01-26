from cores import design
def titulo(texto="", simbolo='~', corTexto='branco', fundo='fundo verde'):
    print(design(simbolo*(len(texto)+4), c=corTexto, b=fundo))
    print(design(f'  {texto}  ', c=corTexto, b=fundo))
    print(design(simbolo*(len(texto)+4), c=corTexto, b=fundo))
def ajuda(texto):
    titulo("Acessando o manual do comando", corTexto='branco', fundo='fundo azul')
    print("\033[7;35m")
    h = help(texto)
    print("\033[m")
    return h

while True:
    titulo('SISTEMA DE AJUDA PyHELP', '~')
    info = str(input("Função ou Biblioteca > ")).strip()    
    if info in "fim":
        break
    ajuda(info)
titulo('ATÉ LOGO!', simbolo='~', corTexto='branco', fundo='fundo vermelho')