from pathlib import Path
import pandas as pd

# Garantindo que o python leia o decimal corretamente
pasta_atual = Path(__file__).parent
tabela_clientes = pd.read_excel(
    pasta_atual / 'clientes.xlsx', sheet_name='SC', header=0, index_col=0, usecols=[2,3], decimal='.')
print(tabela_clientes.head(10))
