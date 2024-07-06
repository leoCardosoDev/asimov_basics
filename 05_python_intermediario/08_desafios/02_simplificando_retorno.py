# Desafio 2
"""
Temos duas funções abaixo que simulam operações em banco de dados:
# - busca_dados: que retorna informações de um banco de dados, mas falha em 50%
    das vezes em que é executada
# - processa_dados, que processa a informação obtida a partir do banco de dados
"""
import random

def simula_busca_dados():
    if random.random() > 0.5:
        return None
    return 'xxxx'

def simula_processa_dados(dados):
    return f'Dados "{dados}" foram processados'

# código verboso
dados_banco_verboso = simula_busca_dados()
if dados_banco_verboso is not None:
    dados_processados_verboso = simula_processa_dados(dados_banco_verboso)
else:
    dados_processados_verboso = 'N/A'
print(f'Verboso: {dados_processados_verboso}')

# Codigo otimizado (menor)
dados_banco_otimizado = simula_busca_dados()
dados_processados_otimizado = (simula_processa_dados(dados_banco_otimizado) if (dados_banco_otimizado := simula_busca_dados()) is not None else 'N/A')
print(f'Otimizado: {dados_processados_otimizado}')
