from pathlib import Path
import pandas as pd

# Modificando header
pasta_atual = Path(__file__).parent
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SC', header=0)
print(tabela_clientes.head(10))
