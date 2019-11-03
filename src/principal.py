"""
@coding: UTF-8
@user: joao-santos
@author: João Paulo Ribeiro dos Santos
@date: 02/11/2019
"""
# Importações
from src.Connection_IBGE import IBGEConnection as cnn
import os

class AcessoAPINomeIBGE:

    def __init__(self, caminho_arquivo):
        self.str_caminho_arquivo_links =  caminho_arquivo
        self.lst_apis_ibge = []

    # Carregar os links
    def fn_captar_strings_conexao_arquivo_csv(self):
        """
        Function: função que retorna uma lista com as string de conexão
    
        Args:
            string: Caminho do arquivo 'links_APIs.csv'
        Return:
            list: lista de string de conexao
        """
    
        content = []
        try:
            with open(self.str_caminho_arquivo_links, "r") as data:
                for line in data:
                    content.append(line.split('\n'))
            data.close()
    
            self.lst_apis_ibge = [i[0] for i in content]
        except FileNotFoundError as fe:
            print("Arquivo '{}' não encontrado.".format(fe.filename))
        except OSError as ose:
            print("Problemas na leitura do arquivo '{}'".format(ose.filename))

    # Funções principais, que permitem trazer as informações da API
    
    def fn_IBGE_buscar_frequencia_um_nome_por_decadas(self, nome):
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
            print('O nome passado não é uma string válida.')
        # Tratar a string de conexão
        url_aux = self.lst_apis_ibge[0]
        url = url_aux[:-7]
        url += nome
        cnx = cnn(url)
    
        # Realizar a solicitação
        num_response, list_info = cnx.get_dados_IBGE()
        return num_response, list_info
    
    def fn_IBGE_buscar_frequencia_lista_nomes_por_decadas(self, list_nomes):
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
        url_aux = self.lst_apis_ibge[0]
        url = url_aux[:-7]
        url += nomes
    
        cnx = cnn(url)
    
        # Realizar a solicitação
        num_response, list_info = cnx.get_dados_IBGE()
        return num_response, list_info
    
    def fn_IBGE_buscar_frequencia_um_nome_e_sexo(self, nome, sexo):
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
            print('O sexo passado deve ser ser "F" ou "M".')
    
        if not isinstance(nome, str):
            print('O nome passado não é uma string válida.')

        # Tratar a string de conexão
        url_aux = self.lst_apis_ibge[1]
        url = url_aux[:]
        url = url.replace('{nomes}',nome)
        url = url.replace('{sexo}', sexo)
    
        cnx = cnn(url)
        # Realizar a solicitação
        num_response, list_info = cnx.get_dados_IBGE()
        return num_response, list_info
    
    def fn_IBGE_listar_ranking_dos_nomes_mais_frequentes(self):
        """
            Function: função que retorna uma lista com o rank dos nomes mais frequentes
    
            Args:
    
            Return:
                int: resposta http
                list: lista com as informações
        """
        # Tratar a string de conexão
        url = self.lst_apis_ibge[4]
    
        cnx = cnn(url)
        # Realizar a solicitação
        num_response, list_info = cnx.get_dados_IBGE()
        return num_response, list_info
    
    def fn_IBGE_listar_ranking_dos_nomes_mais_frequentes_por_decada(self, decada):
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
            print('A década passada deve ser um numero')
    
        if decada not in list_decadas:
            print('A década informada não é válida, insira um valor entre 1900 e \n2100, ' \
                      'considerando um salto de 10 anos, logo a década \n poderia ser: 1900, 1950, ' \
                  '1940, 1990, 2000, etc...')

        # Tratar a string de conexão
        url_aux = self.lst_apis_ibge[5]
        url = url_aux[:]
        url = url.replace('{decada}',str(decada))
    
        cnx = cnn(url)
        # Realizar a solicitação
        num_response, list_info = cnx.get_dados_IBGE()
        return num_response, list_info
    
    def fn_IBGE_listar_ranking_dos_nomes_mais_frequentes_por_sexo(self, sexo):
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
            print('O sexo informado não é uma string.')
    
        if sexo not in 'fmFM':
            print('O sexo informado não é M(Masculino) ou F(Feminino)')
    
        # Tratar a string de conexão
        url_aux = self.lst_apis_ibge[7]
        url = url_aux[:]
        url = url.replace('{sexo}',sexo)
    
        cnx = cnn(url)
        # Realizar a solicitação
        num_response, list_info = cnx.get_dados_IBGE()
        return num_response, list_info


