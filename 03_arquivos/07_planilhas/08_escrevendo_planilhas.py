from pathlib import Path
import pandas as pd

# Criando uma cópia da planilha
pasta_atual = Path(__file__).parent
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx')
tabela_clientes.to_excel(pasta_atual / 'copia_clientes.xlsx')
ler_nova_panilha = pd.read_excel(pasta_atual / 'copia_clientes.xlsx')
print(ler_nova_panilha.head(10))
