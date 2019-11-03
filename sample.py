"""
@coding: UTF-8
@user: joao-santos
@author: João Paulo Ribeiro dos Santos
@date: 03/11/2019
"""
from src.principal import AcessoAPINomeIBGE

# Captar as informações das string de conexão
links = 'data/links_APIs.csv'
pr = AcessoAPINomeIBGE(links)
pr.fn_captar_strings_conexao_arquivo_csv()

# Mostrar as strings de conexão
#print(pr.lst_apis_ibge)

# Listar os nomes mais frequentes por decada

int_response, lst_names_ranking = pr.fn_IBGE_listar_ranking_dos_nomes_mais_frequentes_por_decada(1960)
print(lst_names_ranking)

