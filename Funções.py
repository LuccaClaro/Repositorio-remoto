def normaliza(dicio):
    banco_de_dados = {}
    for c, v in dicio.items():
        for c2, v2 in v.items():
            banco_de_dados[c2] = v2
            banco_de_dados[c2]["continente"]=c

    return banco_de_dados