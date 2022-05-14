import Funções
import Dados
import unicodedata
import random

continuar = "s"
while continuar == "s":
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
    print("")
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

    print(f"{fg.yellow}Modos de jogo: Normal|n|, Bandeira|b|, Capitais|c|{reset}\n")
    modo_jogo = input("Escolha um modo de jogo |n|b|c|: ")
    print("============================================================================================================================================")
    
    if modo_jogo == "c":
        print("")
        print("Nesse modo você receberá o nome da capital e o continente e deverá acertar o país, o jogo continua até você errar\n")
        cond = True
        pontuação = 0
        while cond != False:
            capital_pais_escolhido = banco_de_dados[pais_escolhido]["capital"]
            continente_pais_escolhido = banco_de_dados[pais_escolhido]['continente']
            print(f"Sua pontuação:{fg.pink}{pontuação}{reset}")
            original = input(f"Qual é o país cuja capital capital é {fg.pink}{capital_pais_escolhido}{reset} e o continente é {fg.pink}{continente_pais_escolhido}{reset}?: ")
            processamento_2 = unicodedata.normalize("NFD", original)
            processamento_2 = processamento_2.encode("ascii", "ignore")
            processamento_2 = processamento_2.decode("utf-8")
            tentativa = processamento_2.lower()
            print("")
            if tentativa in lista_paises:
                if tentativa == pais_escolhido:
                    print(f"{bcolors.OKGREEN}Correto{reset}")
                    print("")
                    pontuação += 1
                    lista_paises.remove(pais_escolhido)
                    pais_escolhido = (random.choice(lista_paises))
                else:
                    print(f"{bcolors.FAIL}Incorreto, a resposta era {fg.pink}{pais_escolhido}{reset}\n")
                    print(f"Pontuação final {fg.pink}{pontuação}{reset}")
                    break
            elif tentativa == "desisto":
                certeza = input("Você quer desistir mesmo? |s|n|: ")
                if certeza == "s":
                    print(f"{bcolors.ENDC}-------------------------------------------------------------------")
                    print(f"{bcolors.FAIL}Folgado, a resposta era {pais_escolhido}")
                    print(f"{bcolors.ENDC}-------------------------------------------------------------------")
                    break
            else:
                print("País desconhecido")
            print("============================================================================================================================================")
        print("")
        continuar = input("Quer jogar novamente? |s|n|: ")

    if modo_jogo == "b":
        print(f"{bcolors.ENDC}Um país foi escolhido dentro de {len(lista_paises)} países, tente advinhar!")
        print("")
        tentativas = 8
        print("Nesse modo você terá que advinhar o país apartir apenas pelas cores de sua bandeira, sem dicas\n")
        valor = 0
        for c,v in banco_de_dados[pais_escolhido]["bandeira"].items():
            if v>0:
                if c == "vermelha":
                    d = f"{bcolors.FAIL}{c}{reset}({v}%)"
                elif c == "laranja":
                    d = f"{fg.red}{c}{reset}({v}%)"
                elif c == "amarela":
                    d = f"{fg.yellow}{c}{reset}({v}%)"
                elif c == "verde":
                    d = f"{fg.green}{c}{reset}({v}%)"
                elif c == "azul":
                    d = f"{fg.blue}{c}{reset}({v}%)"
                elif c == "azul claro":
                    d = f"{fg.cyan}{c}{reset}({v}%)"
                elif c == "preta":
                    d = f"{fg.black}{c}{reset}({v}%)"
                elif c == "branca":
                    d = f"{c}({v}%)"
                elif c == "outras":
                    d = f"{reverse}{c}{reset}({v}%)"
                cores_da_bandeira_lista.append(d)
        cores_da_bandeira_juntas = (', '.join(cores_da_bandeira_lista))
        atalho = (f"{cores_da_bandeira_juntas}")
        while tentativas > 0:
            print(f"{bcolors.ENDC}-----------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"A bandeira do pais possui {atalho}\n")
            print(f"O continente é {continente_pais_escolhido}")
            print (f"{bcolors.ENDC}Você tem {fg.pink}{tentativas}{bcolors.ENDC} tentativa(s)")
            print("")
            original = input(f"{bcolors.ENDC}Qual seu palpite?: ")
            print("")
            print("")
            print("")
            processamento_2 = unicodedata.normalize("NFD", original)
            processamento_2 = processamento_2.encode("ascii", "ignore")
            processamento_2 = processamento_2.decode("utf-8")
            pergunta_inicial = processamento_2.lower()
            print(f"{bcolors.ENDC}===========================================================================================================================================================")
            if pergunta_inicial in lista_paises:
                    if pergunta_inicial == pais_escolhido:
                        tentativas -= 1
                        print(f"{bcolors.ENDC}-------------------------------------------------------------------")
                        print(f"{bcolors.OKGREEN}Parabens, você acertou restando {tentativas} tentativa(s)! O país era {pais_escolhido}")
                        print(f"{bcolors.ENDC}-------------------------------------------------------------------")
                        break
                    else:
                        if pergunta_inicial not in paises_chutados:
                            tentativas -= 1
                            paises_chutados.append(pergunta_inicial)
                            latitude = banco_de_dados[pergunta_inicial]["geo"]["latitude"]
                            longitude = banco_de_dados[pergunta_inicial]["geo"]["longitude"]
                            distancia = Funções.haversine(Dados.EARTH_RADIUS,latitude_pais_escolhido,longitude_pais_escolhido,latitude,longitude)
                            Funções.adiciona_em_ordem(pergunta_inicial,distancia,distancias_mais_perto)
                            print("Distâncias:")
                            print("------------------------------------------")
                            espaço = ""
                            for l in distancias_mais_perto:
                                d = int(l[1])
                                wq = ("{:,}".format(d).replace(',','.'))
                                if l[0] == pergunta_inicial:
                                    if d<1000:
                                        print(f"{fg.lightblue}{underline}{bold} {espaço:3}{wq} km --> {l[0]}")
                                    if d>=1000 and d<10000:
                                        print(f"{fg.yellow}{underline}{bold} {espaço:1}{wq} km --> {l[0]}")
                                    if d>=10000:
                                        print(f"{fg.lightred}{underline}{bold} {wq:3} km --> {l[0]}")
                                else:
                                    if d<1000:
                                        print(f"{reset}{fg.lightblue} {espaço:3}{wq} km --> {l[0]}")
                                    if d>=1000 and d<10000:
                                        print(f"{reset} {fg.yellow} {wq:4} km --> {l[0]}")
                                    if d>=10000:
                                        print(f"{reset}{fg.lightred} {wq:3} km --> {l[0]}")
                            print(f"{bcolors.ENDC}------------------------------------------")
                        else:
                            print(f"{fg.yellow}Você já escolheu esse país{reset}")
                            print("")
            elif pergunta_inicial == "desisto":
                certeza = input("Você quer desistir mesmo? |s|n|: ")
                if certeza == "s":
                    print(f"{bcolors.ENDC}-------------------------------------------------------------------")
                    print(f"{bcolors.FAIL}Folgado, a resposta era {pais_escolhido}")
                    print(f"{bcolors.ENDC}-------------------------------------------------------------------")
                    tentativas = 0
                    desistiu = "sim"
            elif pergunta_inicial == "inventario":
                print("Distâncias:")
                print("------------------------------------------")
                for l in distancias_mais_perto:
                    d = int(l[1])
                    wq = ("{:,}".format(d).replace(',','.'))
                    if l[0] == pergunta_inicial:
                        if d<1000:
                            print(f"{fg.lightblue}{underline}{bold} {espaço:3}{wq} km --> {l[0]}")
                        if d>=1000 and d<10000:
                            print(f"{fg.yellow}{underline}{bold} {espaço:1}{wq} km --> {l[0]}")
                        if d>=10000:
                            print(f"{fg.lightred}{underline}{bold} {wq:3} km --> {l[0]}")
                    else:
                        if d<1000:
                            print(f"{reset}{fg.lightblue} {espaço:3}{wq} km --> {l[0]}")
                        if d>=1000 and d<10000:
                            print(f"{reset} {fg.yellow} {wq:4} km --> {l[0]}")
                        if d>=10000:
                            print(f"{reset}{fg.lightred} {wq:3} km --> {l[0]}")
            elif pergunta_inicial not in lista_paises:
                print("País desconhecido")
        if desistiu != "sim" and tentativas == 0:
            print(f"{bcolors.ENDC}-------------------------------------------------------------------")
            print(f"{bcolors.FAIL}Não foi dessa vez :(     A resposta era {pais_escolhido}")
            print(f"{bcolors.ENDC}-------------------------------------------------------------------")
        continuar = input("Quer jogar novamente? |s|n|: ")



    if modo_jogo == "n":
        print ("")
        print(f"{bcolors.ENDC}Um país foi escolhido dentro de {len(lista_paises)} países, tente advinhar!")
        tentativas = 20
        while tentativas > 0: 
            print (f"{bcolors.ENDC}Você tem {fg.pink}{tentativas}{bcolors.ENDC} tentativa(s)") 
            print("")
            original = input(f"{bcolors.ENDC}Qual seu palpite?: ")
            print("")
            print("")
            print("")
            processamento_2 = unicodedata.normalize("NFD", original)
            processamento_2 = processamento_2.encode("ascii", "ignore")
            processamento_2 = processamento_2.decode("utf-8")
            pergunta_inicial = processamento_2.lower()

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
                print("")
                if dica_escolhida == "0" or dica_escolhida == "1" or dica_escolhida == "2" or dica_escolhida == "3" or dica_escolhida == "4":
                    if dica_escolhida not in dicas_usadas:
                        if tentativas - (int(dica_escolhida) + 3) > 0:
                            tentativas -= (int(dica_escolhida) + 3)

                            #Dica 0
                            if int(dica_escolhida) == 0:
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
                            print("Distâncias:") 
                            print("------------------------------------------")
                            espaço = ""  
                            for l in distancias_mais_perto:
                                d = int(l[1])
                                wq = ("{:,}".format(d).replace(',','.'))
                                if l[0] == pergunta_inicial:
                                    if d<1000:
                                        print(f"{fg.lightblue}{underline}{bold} {espaço:3}{wq} km --> {l[0]}")
                                    if d>=1000 and d<10000:
                                        print(f"{fg.yellow}{underline}{bold} {espaço:1}{wq} km --> {l[0]}")
                                    if d>=10000:
                                        print(f"{fg.lightred}{underline}{bold} {wq:3} km --> {l[0]}")          
                                    else:
                                        if d<1000:
                                            print(f"{reset}{fg.lightblue} {espaço:3}{wq} km --> {l[0]}")
                                        if d>=1000 and d<10000:
                                            print(f"{reset} {fg.yellow} {wq:4} km --> {l[0]}")
                                        if d>=10000:
                                            print(f"{reset}{fg.lightred} {wq:3} km --> {l[0]}")
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
            elif pergunta_inicial in lista_paises:
                if pergunta_inicial == pais_escolhido:
                    tentativas -= 1
                    print(f"{bcolors.ENDC}-------------------------------------------------------------------")
                    print(f"{bcolors.OKGREEN}Parabens, você acertou restando {tentativas} tentativa(s)! O país era {pais_escolhido}")
                    print(f"{bcolors.ENDC}-------------------------------------------------------------------")
                    break
                else:
                    if pergunta_inicial not in paises_chutados:
                        tentativas -= 1
                        paises_chutados.append(pergunta_inicial)
                        latitude = banco_de_dados[pergunta_inicial]["geo"]["latitude"]
                        longitude = banco_de_dados[pergunta_inicial]["geo"]["longitude"]
                        distancia = Funções.haversine(Dados.EARTH_RADIUS,latitude_pais_escolhido,longitude_pais_escolhido,latitude,longitude)
                        Funções.adiciona_em_ordem(pergunta_inicial,distancia,distancias_mais_perto)
                        print("Distâncias:") 
                        print("------------------------------------------")
                        espaço = ""  
                        for l in distancias_mais_perto:
                            d = int(l[1])
                            wq = ("{:,}".format(d).replace(',','.'))
                            if l[0] == pergunta_inicial:
                                if d<1000:
                                    print(f"{fg.lightblue}{underline}{bold} {espaço:3}{wq} km --> {l[0]}")
                                if d>=1000 and d<10000:
                                    print(f"{fg.yellow}{underline}{bold} {espaço:1}{wq} km --> {l[0]}")
                                if d>=10000:
                                    print(f"{fg.lightred}{underline}{bold} {wq:3} km --> {l[0]}")          
                            else:
                                if d<1000:
                                    print(f"{reset}{fg.lightblue} {espaço:3}{wq} km --> {l[0]}")
                                if d>=1000 and d<10000:
                                    print(f"{reset} {fg.yellow} {wq:4} km --> {l[0]}")
                                if d>=10000:
                                    print(f"{reset}{fg.lightred} {wq:3} km --> {l[0]}")
                        print(f"{bcolors.ENDC}------------------------------------------")
                        print(f"{bcolors.ENDC}Dicas:")
                        print(f"{bcolors.ENDC}-----------------------------------------------------------------------------------------------------------------------------------------------------------")
                        for q in dicas_compradas:
                            if q == atalho:
                                print(f"{bcolors.OKBLUE}{q}")
                            else:
                                print(q)
                        print(f"{bcolors.ENDC}-----------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("")
                    else:
                        print("Você já escolheu esse país")
                        print("")
            elif pergunta_inicial == "desisto":
                certeza = input("Você quer desistir mesmo? |s|n|: ")
                if certeza == "s":
                    print(f"{bcolors.ENDC}-------------------------------------------------------------------")
                    print(f"{bcolors.FAIL}Folgado, a resposta era {pais_escolhido}")
                    print(f"{bcolors.ENDC}-------------------------------------------------------------------")
                    tentativas = 0
                    desistiu = "sim"
            elif pergunta_inicial == "inventario":
                print("Distâncias:")  
                print("------------------------------------------") 
                for l in distancias_mais_perto:
                    d = int(l[1])
                    wq = ("{:,}".format(d).replace(',','.'))
                    if l[0] == pergunta_inicial:
                        if d<1000:
                            print(f"{fg.lightblue}{underline}{bold} {espaço:3}{wq} km --> {l[0]}")
                        if d>=1000 and d<10000:
                            print(f"{fg.yellow}{underline}{bold} {espaço:1}{wq} km --> {l[0]}")
                        if d>=10000:
                            print(f"{fg.lightred}{underline}{bold} {wq:3} km --> {l[0]}")          
                        else:
                            if d<1000:
                                print(f"{reset}{fg.lightblue} {espaço:3}{wq} km --> {l[0]}")
                            if d>=1000 and d<10000:
                                print(f"{reset} {fg.yellow} {wq:4} km --> {l[0]}")
                            if d>=10000:
                                print(f"{reset}{fg.lightred} {wq:3} km --> {l[0]}")
                print(f"{bcolors.ENDC}------------------------------------------")
                print("")
                print("Dicas:")
                print(f"{bcolors.ENDC}------------------------------------------")
                for q in dicas_compradas:
                    print(q)
                print(f"{bcolors.ENDC}------------------------------------------")
            elif pergunta_inicial not in lista_paises:
                print("País desconhecido")
        if desistiu != "sim" and tentativas == 0:
            print(f"{bcolors.ENDC}-------------------------------------------------------------------")
            print(f"{bcolors.FAIL}Não foi dessa vez :(     A resposta era {pais_escolhido}")
            print(f"{bcolors.ENDC}-------------------------------------------------------------------")
        continuar = input("Quer jogar novamente? |s|n|: ")