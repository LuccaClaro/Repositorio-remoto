import random

def normaliza(dicio):
    banco_de_dados = {}
    for c, v in dicio.items():
        for c2, v2 in v.items():
            banco_de_dados[c2] = v2
            banco_de_dados[c2]["continente"]=c

    return banco_de_dados

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

def sorteia_letra(palavra,lista):
    especial = ['.', ',', '-', ';', ' ']
    final = []
    p = palavra.lower()
    for i in p:
        if i not in especial and i not in lista and i not in final:
            final.append(i)
    if final == []:
          return ""
    else:
        return (random.choice(final))

def adiciona_em_ordem(a,b,l):
    n=0
    for i in range (0, len (l)):
        if l[i][1] < b:
            n = i + 1
    l. insert (n, [a,b])
    return l