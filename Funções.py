def normaliza(dicio):
    banco_de_dados = {}
    for c, v in dicio.items():
        for c2, v2 in v.items():
            banco_de_dados[c2] = v2
            banco_de_dados[c2]["continente"]=c

    return banco_de_dados

import random
def sorteia_pais(dicio):
    lista_paises = []
    for i in dicio.keys():
        lista_paises.append(i)
    return (random.choice(lista_paises))

def esta_na_lista(pais, lista):
    for a in lista:
        for i in a:
            if pais in str(i):
                return True
    return False