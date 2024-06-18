from pathlib import Path

# Lendo um arquivo (Forma recomendada)
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
  print(lista_compras.read())
