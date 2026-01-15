'''pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}
print(pessoas) #{"nome": "Gustavo", "sexo": "M", "idade": 22}
print(pessoas['nome']) #Gustavo
print(pessoas['idade']) #22
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.") #O Gustavo tem 22 anos.
print(pessoas.keys()) #dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) #dict_values(['Gustavo', 'M', 22])
print(pessoas.items()) #dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
for k in pessoas.keys():
    print(k)
    """
    nome
    sexo
    idade
    """
for k in pessoas.values():
    print(k)
    """
    Gustavo
    M
    22
    """
for k, v in pessoas.items():
    print(f"{k} = {v}")
    """
    nome = Gustavo
    sexo = M
    idade = 22
    """
"""
#Apagando o sexo do dicionário
del pessoas['sexo']
for k, v in pessoas.items():
    print(f"{k} = {v}")
    
    #nome = Gustavo
    #idade = 22
"""
"""
#Modificando info existentes
pessoas['nome'] = "Leandro"
for k, v in pessoas.items():
    print(f"{k} = {v}")
    #nome = Leandro
    #sexo = M
    #idade = 22
"""
"""
#Adicionando elementos no dicionário
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f"{k} = {v}")
    #nome = Gustavo
    #sexo = M
    #idade = 22
    #peso = 98.5
"""
'''

"""
#Dicionario dentro de lista / Lista com dicionários
brasil = []
estado1 = {'uf': 'Rio de Janeiro', "sigla": "RJ"}
estado2 = {'uf': 'São Paulo', "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
#print(estado1) #{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#print(estado2) #{'uf': 'São Paulo', "sigla": "SP"}
#print(brasil) #[{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
#print(brasil[0]) #{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#print(brasil[1]) #{'uf': 'São Paulo', "sigla": "SP"}
#print(brasil[0]['uf']) #Rio de Janeiro
#print(brasil[1]['sigla']) #SP

"""
"""
estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input("Unidade federativa: ")).strip().capitalize()
    estado['sigla'] = str(input("Sigla de Estado: ")).strip().upper()
    brasil.append(estado)
print(brasil) #Deu erro
#[{'uf': 'Minas gerais', 'sigla': 'MG'}, {'uf': 'Minas gerais', 'sigla': 'MG'}, {'uf': 'Minas gerais', 'sigla': 'MG'}]
"""
"""
estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input("Unidade federativa: ")).strip().capitalize()
    estado['sigla'] = str(input("Sigla de Estado: ")).strip().upper()
    brasil.append(estado[:])
print(brasil)
''' Erro esperado
brasil.append(estado[:])
              ~~~~~~^^^
KeyError: slice(None, None, None)'''"""
"""
estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input("Unidade federativa: ")).strip().capitalize()
    estado['sigla'] = str(input("Sigla de Estado: ")).strip().upper()
    brasil.append(estado.copy()) #O método copy() copia um elemento do dicionário para a lista.
#print(brasil) #[{'uf': 'São paulo', 'sigla': 'SP'}, {'uf': 'Rio de janeiro', 'sigla': 'RJ'}, {'uf': 'Espírito santo', 'sigla': 'ES'}]
for e in brasil:
    print(e)
    '''
    {'uf': 'Rio', 'sigla': 'RJ'}
    {'uf': 'Sampa', 'sigla': 'SP'}
    {'uf': 'Paraná', 'sigla': 'PR'}
    '''
"""
"""estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input("Unidade federativa: ")).strip().capitalize()
    estado['sigla'] = str(input("Sigla de Estado: ")).strip().upper()
    brasil.append(estado.copy()) #O método copy() copia um elemento do dicionário para a lista.
#print(brasil) #[{'uf': 'São paulo', 'sigla': 'SP'}, {'uf': 'Rio de janeiro', 'sigla': 'RJ'}, {'uf': 'Espírito santo', 'sigla': 'ES'}]
for e in brasil: #for da lista
    for k, v in e.items(): #chave e valor no e (cada dicionário)
        print(f"O campo {k} tem valor {v}.")
'''
O campo uf tem valor Rio.
O campo sigla tem valor RJ.
O campo uf tem valor Sampa.
O campo sigla tem valor SP.
O campo uf tem valor Goias.
O campo sigla tem valor GO.
'''"""       

estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input("Unidade federativa: ")).strip().capitalize()
    estado['sigla'] = str(input("Sigla de Estado: ")).strip().upper()
    brasil.append(estado.copy()) #O método copy() copia um elemento do dicionário para a lista.
#print(brasil) #[{'uf': 'São paulo', 'sigla': 'SP'}, {'uf': 'Rio de janeiro', 'sigla': 'RJ'}, {'uf': 'Espírito santo', 'sigla': 'ES'}]
for e in brasil: #for da lista
    for v in e.values(): #chave e valor no e (cada dicionário)
        print(v, end=" ")
    print()
#Rio RJ 
#Sampa SP
#Bahia BH