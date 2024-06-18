from pathlib import Path

# Escrevendo linha a linha
pasta_atual = Path(__file__).parent
novos_itens = ['banana', 'abacate', 'abacaxi']
novos_items_com_quebra_de_linha = [f'\n{item}' for item in novos_itens]
# for item in novos_itens:
#   novos_items_com_quebra_de_linha.append(f'\n{item}')
with open(pasta_atual / 'add_lista_de_compras.txt', mode='a') as nova_lista_de_compras:
  nova_lista_de_compras.writelines(novos_items_com_quebra_de_linha)

