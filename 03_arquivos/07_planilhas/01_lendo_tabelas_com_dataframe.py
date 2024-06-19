from pathlib import Path
import pandas as pd

# Lendo tabelas com Dataframe
pasta_atual = Path(__file__).parent
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx')
# 10 primeiros elementos
print(tabela_clientes.head(10)) 
