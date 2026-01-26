def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    grupo = {}
    grupo['total'] = len(n)
    grupo['maior'] = max(n)
    grupo['menor'] = min(n)
    grupo['média'] = sum(n) / len(n)
    if sit == True:
        if grupo['média'] >= 7:
            grupo['situação'] = "BOA"
        elif grupo['média'] >= 5 and grupo['média'] < 7:
            grupo['situação'] = "RAZOÁVEL"
        else:
            grupo['situação'] = "RUIM"
    return grupo

#resp = notas(5.5, 9.5, 10, 6.5)
resp = notas(9, 2.1, 1, 3, sit=True)
print(resp)
#help(notas)
