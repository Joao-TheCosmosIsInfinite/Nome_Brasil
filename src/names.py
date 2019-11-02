"""
@coding: UTF-8
@user: joao-santos
@author: João Paulo Ribeiro dos Santos
@date: 01/11/2019
"""

# Classe
class Names():
    """
        Classe relacionada ao(s) nome(s) a ser(em) pesquisado(s)

        Essa classe tem todas as informações e métodos resposáveis pela pesquisa e manipulação da API de nomes do IBGE
    """
    def __init__(self, names):
        """
        Constructor

        Args:
            url: O endereço URL da API do IBGE
        """
        self.names = names
        self.sexo = None

    def fn_trata_multiplos_nomes(self, names):
        """
        Function: receber uma lista de nomes e retornar esses nomes como uma string, separada
            por '|'(pipe) cada nome

        Args: list: uma lista com nomes

        Return:
              string: nomes separados por '|' (pipe)
        """
        if not isinstance(names, list):
            return 0
        return '|'.join(names)

    def fn_trata_sexo(self, sexo):
        """
        Function: recebe uma string com o sexo da pessoa:
                    M : Masculino
                    F : Feminino

        Args:
            string: sexo do individuo pesquisado

        Return:
              string: sexo M ou F de acordo com o passado
        """
        if sexo in 'fmFM':
            return sexo.upper()
        else:
            return 0
