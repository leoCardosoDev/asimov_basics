from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent
tabela_clientes_dict = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name=None)
for nome_aba, tabela in tabela_clientes_dict.items():
  tabela.to_excel(pasta_atual / 'planilhas' / 'planilhas_separadas' / f'{nome_aba.lower()}.xlsx')
