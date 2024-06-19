from pathlib import Path
import pandas as pd

# Criando uma cópia da planilha com várias abas
pasta_atual = Path(__file__).parent
tabela_clientes_sc = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name="SC")
tabela_clientes_sp = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name="SP")
tabela_clientes_rs = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name="RS")

with pd.ExcelWriter(pasta_atual / 'abas_planilhas.xlsx') as nova_planilha:
  tabela_clientes_sc.to_excel(nova_planilha, sheet_name='SC', index=False)
  tabela_clientes_sp.to_excel(nova_planilha, sheet_name='SP', index=False)
  tabela_clientes_rs.to_excel(nova_planilha, sheet_name='RS', index=False)

ler_nova_panilha = pd.read_excel(pasta_atual / 'abas_planilhas.xlsx')
print(ler_nova_panilha)
