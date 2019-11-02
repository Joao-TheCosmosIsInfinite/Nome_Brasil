"""
@coding: UTF-8
@user: joao-santos
@author: João Paulo Ribeiro dos Santos
@date: 02/11/2019
"""
# Importações
from src.Connection_IBGE import IBGEConnection as cnn
import os

# Carregar os links
def __fn_lista_strings_conexao():
    """
    Function: função que retorna uma lista com as string de conexão

    Args:

    Return:
        list: lista de string de conexao
    """
    # Caminho onde esta o projeto exlcuindo a pasta SRC
    diretorio_raiz = os.path.abspath(os.curdir)
    arquivo = diretorio_raiz[:-3]

    # Aplicando a pasta data e o arquivo a string
    arquivo += 'data/links_APIs.csv'
    content = []
    try:
        with open(arquivo, "r") as data:
            for line in data:
                content.append(line.split('\n'))
        data.close()

        lists = [i[0] for i in content]
        return lists
    except FileNotFoundError as fe:
        print("Arquivo '{}' não encontrado.".format(fe.filename))
    except OSError as ose:
        print("Problemas na leitura do arquivo '{}'".format(ose.filename))

# Variavel com os Links
lst_links =  __fn_lista_strings_conexao()

# Funções principais, que permitem trazer as informações da API

def fn_IBGE_buscar_frequencia_um_nome_por_decadas(nome):
    """
        Function: função que retorna uma lista com as decadas com a frequencia de um nome passado

        Args:
            string: nome a ser pesquisado

        Return:
            int: resposta http
            list: lista com as informações da frequencia do nome
    """
    # Validar Entradas
    if not isinstance(nome, str):
        return 0, 'O nome passado não é uma string válida.'
    # Tratar a string de conexão
    url_aux = lst_links[0]
    url = url_aux[:-7]
    url += nome
    cnx = cnn(url)

    # Realizar a solicitação
    num_response, list_info = cnx.get_dados_IBGE()
    return num_response, list_info

def fn_IBGE_buscar_frequencia_lista_nomes_por_decadas(list_nomes):
    """
        Function: função que retorna uma lista com as decadas com a frequencia de uma lista
        de nomes passadis

        Args:
            string list: lista de string

        Return:
            int: resposta http
            list: lista com as informações da frequencia dos nomes
    """
    if not isinstance(list_nomes, list):
        return 0, 'O objeto passado não é uma lista'

    # Remover nome a nome da lista e colocá-los em uma string, separando-os por '|'
    nomes = '|'.join(list_nomes)

    # Tratar a string de conexão
    url_aux = lst_links[0]
    url = url_aux[:-7]
    url += nomes

    cnx = cnn(url)

    # Realizar a solicitação
    num_response, list_info = cnx.get_dados_IBGE()
    return num_response, list_info

def fn_IBGE_buscar_frequencia_um_nome_e_sexo(nome, sexo):
    """
        Function: função que retorna uma lista com as decadas com a frequencia de um nome passado

        Args:
            string: nome a ser pesquisado
            string: sexo a ser passado
        Return:
            int: resposta http
            list: lista com as informações da frequencia do nome
    """
    # Validar entradas
    if sexo not in 'fmFM':
        return 0, 'O sexo passado deve ser ser "F" ou "M".'

    if not isinstance(nome, str):
        return 0, 'O nome passado não é uma string válida.'
    ## 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nomes}?sexo=M'


    # Tratar a string de conexão
    url_aux = lst_links[1]
    url = url_aux[:]
    url = url.replace('{nomes}',nome)
    url = url.replace('{sexo}', sexo)

    cnx = cnn(url)
    # Realizar a solicitação
    num_response, list_info = cnx.get_dados_IBGE()
    return num_response, list_info

def fn_IBGE_listar_ranking_dos_nomes_mais_frequentes():
    """
        Function: função que retorna uma lista com o rank dos nomes mais frequentes

        Args:

        Return:
            int: resposta http
            list: lista com as informações
    """
    # Tratar a string de conexão
    url = lst_links[4]

    cnx = cnn(url)
    # Realizar a solicitação
    num_response, list_info = cnx.get_dados_IBGE()
    return num_response, list_info

def fn_IBGE_listar_ranking_dos_nomes_mais_frequentes_por_decada(decada):
    """
        Function: função que retorna uma lista com os nomes mais frequentes usados em uma determinada decada

        Args:
            int: decada a ser pesquisada
        Return:
            int: resposta http
            list: lista com as informações da frequencia do nome
    """
    # Validar entradas
    list_decadas = [x for x in range(1900, 2100, 10)]
    if not isinstance(decada, int):
        return 0, 'A década passada deve ser um numero'

    if decada not in list_decadas:
        return 0, 'A década informada não é válida, insira um valor entre 1900 e \n2100, ' \
                  'considerando um salto de 10 anos, logo a década \n poderia ser: 1900, 1950, 1940, 1990, 2000, etc...'
    ## 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nomes}?sexo=M'


    # Tratar a string de conexão
    url_aux = lst_links[5]
    url = url_aux[:]
    url = url.replace('{decada}',decada)

    cnx = cnn(url)
    # Realizar a solicitação
    num_response, list_info = cnx.get_dados_IBGE()
    return num_response, list_info

def fn_IBGE_listar_ranking_dos_nomes_mais_frequentes_por_sexo(sexo):
    """
        Function: função que retorna uma lista com os nomes mais frequentes usados de acordo com o sexo

        Args:
            string: Sexo M ou F a ser pesquisado
        Return:
            int: resposta http
            list: lista com as informações da frequencia do nome
    """
    # Validar entradas

    if not isinstance(sexo, str):
        return 0, 'O sexo informado não é uma string.'

    if sexo not in 'fmFM':
        return 0, 'O sexo informado não é M(Masculino) ou F(Feminino)'

    # Tratar a string de conexão
    url_aux = lst_links[7]
    url = url_aux[:]
    url = url.replace('{sexo}',sexo)

    cnx = cnn(url)
    # Realizar a solicitação
    num_response, list_info = cnx.get_dados_IBGE()
    return num_response, list_info


