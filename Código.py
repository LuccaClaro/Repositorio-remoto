import Funções
import Dados

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
class fg:
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'
class bg:
    black='\033[40m'
    red='\033[41m'
    green='\033[42m'
    orange='\033[43m'
    blue='\033[44m'
    purple='\033[45m'
    cyan='\033[46m'
    lightgrey='\033[47m'

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

print (f"{bcolors.HEADER}================================\n"
"|                              |\n"
"| Bem-vindo ao jogo dos países |\n"
"|                              |\n"
"=======Design de Software=======\n")
print("")
print (f"{bcolors.ENDC}Comandos:\n"
"                                         \n"
"   dica       - entra no mercado de dicas\n"
"   desisto    - desiste da rodada\n"
"   inventario - exibe sua posição\n")
print(f"Observações:\n"
"    Todos os países estão com letra minúscula e sem acentuação")
print("")
O = "0. Letra da capital   - custa 3 tentativas"
I = "1. Cor da bandeira   - custa 4 tentativas"
II = "2. População        - custa 5 tentativas"
III = "3. Área              - custa 6 tentativas"
IV = "4. Continente         - custa 7 tentativas"
V = "5. Voltar"
lista = [O,I,II,III,IV,V]
dicas_usadas = []
dicas_compradas = []
paises_chutados = []
distancias_mais_perto = []
cores_da_bandeira_lista =[]
lista_restrição_letras =[]
lista_letras = []
contador_cor = 1
desistiu = "não"
contador_letra = 1

print(f"{bcolors.ENDC}Um país foi escolhido dentro de {len(lista_paises)} países, tente advinhar!")
tentativas = 20
while tentativas > 0: 
    print (f"{bcolors.ENDC}Você tem {fg.pink}{tentativas}{bcolors.ENDC} tentativa(s)") 
    print("")
    pergunta_inicial = input(f"{bcolors.ENDC}Qual seu palpite?: ")
    print(f"{bcolors.ENDC}===========================================================================================================================================================")
    if pergunta_inicial == "dica" or pergunta_inicial == "dicas":
        dicas = ("Dicas disponíveis:\n"
        "------------------------------------------\n"
        f"{lista[0]}\n"
        f"{lista[1]}\n"
        f"{lista[2]}\n"
        f"{lista[3]}\n"
        f"{lista[4]}\n"
        f"{lista[5]}\n"
        "------------------------------------------\n")
        print(dicas)
        dica_escolhida = (input("Escolha a dica [0|1|2|3|4|5]: "))
        if dica_escolhida == "0" or dica_escolhida == "1" or dica_escolhida == "2" or dica_escolhida == "3" or dica_escolhida == "4":
            if dica_escolhida not in dicas_usadas:
                if tentativas - (int(dica_escolhida) + 3) > 0:
                    tentativas -= (int(dica_escolhida) + 3)

                    #Dica 0
                    if int(dica_escolhida) == 0:
                        import random
                        letra_capital_pais_escolhido = Funções.sorteia_letra(banco_de_dados[pais_escolhido]["capital"],lista_restrição_letras)
                        lista_letras.append(letra_capital_pais_escolhido)
                        if letra_capital_pais_escolhido != "":
                            if contador_letra > 1:
                                dicas_compradas.remove(f"Letra(s) da capital: {letras_juntas}")
                            lista_restrição_letras.append(letra_capital_pais_escolhido)
                            letras_juntas = (', '.join(lista_letras))
                            atalho = (f"Letra(s) da capital: {letras_juntas}")
                            dicas_compradas.append(atalho)
                            contador_letra += 1
                        if letra_capital_pais_escolhido == "":
                            print("")
                            print(f"{bcolors.ENDC}===========================================================================================================================================================")
                            print(f"{bcolors.FAIL} Não há mais letras...")
                            tentativas += (int(dica_escolhida) + 3)
                            lista[int(dica_escolhida)] = ""
                            dicas_usadas.append(dica_escolhida)

                    #Dica 1
                    if int(dica_escolhida) == 1:
                        valor = 0
                        for c,v in banco_de_dados[pais_escolhido]["bandeira"].items():
                            if v>valor and c not in cores_da_bandeira_lista and v>0:
                                valor = v
                                cor_bandeira_pais_escolhido = c
                        if cor_bandeira_pais_escolhido not in cores_da_bandeira_lista:
                            if contador_cor > 1:
                                lu = f"Cor(es) da bandeira: {cores_da_bandeira_juntas}"
                                dicas_compradas.remove(lu)
                            cores_da_bandeira_lista.append(cor_bandeira_pais_escolhido)
                            cores_da_bandeira_juntas = (', '.join(cores_da_bandeira_lista))
                            atalho = (f"Cor(es) da bandeira: {cores_da_bandeira_juntas}")
                            dicas_compradas.append(atalho)
                            contador_cor += 1
                        else:
                            print("")
                            print(f"{bcolors.FAIL} Não há mais cores...")
                            tentativas += (int(dica_escolhida) + 3)
                            lista[int(dica_escolhida)] = ""
                            dicas_usadas.append(dica_escolhida)

                    #Dica 2
                    if int(dica_escolhida) == 2:
                        atalho = ("População do país: {:,} habitantes".format(população_pais_escolhido).replace(',','.'))
                        dicas_compradas.append (atalho)
                        lista[int(dica_escolhida)] = ""
                        dicas_usadas.append(dica_escolhida)

                    #Dica 3
                    if int(dica_escolhida) == 3:
                        atalho = ("Área do país: {:,} km2".format(area_pais_escolhido).replace(',','.'))
                        dicas_compradas.append (atalho)
                        lista[int(dica_escolhida)] = ""
                        dicas_usadas.append(dica_escolhida)

                    #Dica 4
                    if int(dica_escolhida) == 4:
                        atalho = (f'Continente do país: {continente_pais_escolhido}')
                        dicas_compradas.append (atalho)
                        lista[int(dica_escolhida)] = ""
                        dicas_usadas.append(dica_escolhida)

                    print("------------------------------------------")
                    print("")
                    print(f"{bcolors.ENDC}Dicas:")
                    print(f"{bcolors.ENDC}-----------------------------------------------------------------------------------------------------------------------------------------------------------")
                    for q in dicas_compradas:
                        if q == atalho:
                            print(f"{bcolors.OKBLUE}{q}")
                        else:
                            print(q)
                    print(f"{bcolors.ENDC}-----------------------------------------------------------------------------------------------------------------------------------------------------------")
                elif tentativas - (int(dica_escolhida) + 3) <= 0:
                    print("")
                    print(f"{fg.yellow}Você não possui tentativas suficientes para comprar essa dica")
            else:
                print("Esta dica não existe\n")
        elif dica_escolhida == "5":
            print("")
        else:
            print("Esta dica não existe\n")