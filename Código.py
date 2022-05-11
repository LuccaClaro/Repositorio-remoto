import Funções
import Dados

banco_de_dados = Funções.normaliza(Dados.DADOS)

pais_escolhido = Funções.sorteia_pais(banco_de_dados)

lista_paises = []
for i in banco_de_dados.keys():
    lista_paises.append(i)

#Características do país sorteado:
latitude_pais_escolhido = banco_de_dados[pais_escolhido]["geo"]["latitude"]
longitude_pais_escolhido = banco_de_dados[pais_escolhido]["geo"]["longitude"]
população_pais_escolhido = banco_de_dados[pais_escolhido]['populacao']
area_pais_escolhido = banco_de_dados[pais_escolhido]['area']
continente_pais_escolhido = banco_de_dados[pais_escolhido]['continente']