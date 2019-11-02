"""
@coding: UTF-8
@user: joao-santos
@author: João Paulo Ribeiro dos Santos
"""

# Importações
import unittest
from src.Connection_IBGE import IBGEConnection

# Classe
class TestCase(unittest.TestCase):
    """
     Classe de teste unitário

        Essa classe tem o intuito de verificar se a conexão com as principais 
        APIs de consulta de Nomes do IBGE estão funcionando corretamente
    """
    def test_frequencia_nome_joao(self):
        """
           Verificar se o nome joao é localizado na base de dados, e dado
           que é um nome muito comum, e que sempre é retornado pela API
           a reposta deverá ser 200(OK)
        """
        conn = IBGEConnection('https://servicodados.ibge.gov.br/api/v2/censos/nomes/joao')
        num_response, list_names = conn.get_dados_IBGE()
        self.assertEqual(num_response, 200)

    def test_frequencia_nomes_joao_e_maria(self):
        """
            Verificar se o nome joao e maria são localizados na base de dados
        """
        conn = IBGEConnection('https://servicodados.ibge.gov.br/api/v2/censos/nomes/joao|maria')
        num_response, list_names = conn.get_dados_IBGE()
        self.assertEqual(num_response, 200)

    def test_rank_nomes_sexo_masculino(self):
        """
            Verificar se a API fornece o rank dos nomes mais utilizados do sexo masculino
        """
        conn = IBGEConnection('https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?sexo=M')
        num_response, list_names = conn.get_dados_IBGE()
        self.assertEqual(num_response, 200)

if __name__ == '__main__':
    unittest.main()
