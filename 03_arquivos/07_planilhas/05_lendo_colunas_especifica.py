from pathlib import Path
import pandas as pd

# Lendo coluna especifica
pasta_atual = Path(__file__).parent
tabela_clientes = pd.read_excel(
    #pasta_atual / 'clientes.xlsx', sheet_name='SC', header=0, index_col=0, usecols="A:B")
    pasta_atual / 'clientes.xlsx', sheet_name='SC', header=0, index_col=0, usecols=[0,1])
print(tabela_clientes.head(10))
