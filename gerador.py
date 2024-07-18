import random

def gera_numeros():
    soma = random.randint(8, 18)
    primeiro = random.randint(1, soma - 1)
    segundo = soma - primeiro
    terceiro = random.randint(1, soma - 1)
    lista = [primeiro, segundo, terceiro]
    random.shuffle(lista)
    lista.append(soma)
    return [1,2,3,4]
    return lista
