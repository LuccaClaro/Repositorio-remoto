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