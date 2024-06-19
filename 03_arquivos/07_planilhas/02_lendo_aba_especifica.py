from pathlib import Path
import pandas as pd

# Lendo aba especifica
pasta_atual = Path(__file__).parent
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SC')
# 10 primeiros elementos
print(tabela_clientes.head(10))
