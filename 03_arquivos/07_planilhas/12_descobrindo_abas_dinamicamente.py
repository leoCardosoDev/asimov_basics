from pathlib import Path
import pandas as pd

# Caminho para o arquivo Excel
pasta_atual = Path(__file__).parent
arquivo_excel = pasta_atual / 'clientes.xlsx'

# Carregando o arquivo Excel
excel_file = pd.ExcelFile(arquivo_excel)

# Listando todas as abas (nomes das sheets) no arquivo Excel
abas = excel_file.sheet_names
print("Abas disponíveis:", abas)

# Criando um dicionário para armazenar os DataFrames de cada aba
tabelas_clientes = {}

# Lendo cada aba dinamicamente e armazenando no dicionário
for aba in abas:
    tabelas_clientes[aba] = pd.read_excel(arquivo_excel, sheet_name=aba)

# Usando um loop para imprimir cada DataFrame
for aba in abas:
    print(f"DataFrame da aba '{aba}':")
    print(tabelas_clientes[aba])
    print()  # Adiciona uma linha em branco para separar os outputs
