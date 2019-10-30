# Importações
import json
import requests
from sys import exit

# Classe principal
class connection:
    """
        Classe de conexão com a API do IBGE

        Essa classe tem todas as informações e bibliotecas necessárias para conectar em qualquer API do IBGE,
        desde que a URL passada seja valida
    """
    def init(self, url):
        """
        Constructor

        Args:
            url: O endereço URL da API do IBGE
        """
        self.url = url

    def get_dados_IBGE(self):
        """
        Constructor

        Args:

        Return:
             int: Codigo da Requisição Http, ex.: 200, 400, 404, etc ...
             list: Lista com os dados solicitados de acordo com a URL
        """
        response = requests.request("GET", self.url)
        json_response = json.loads(response.content)
        return response.status_code, json_response
