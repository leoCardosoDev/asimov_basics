from pathlib import Path

item_remover = 'Passear com cachorro'
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'view_lista.html') as html:
  linhas_html = html.readlines()
