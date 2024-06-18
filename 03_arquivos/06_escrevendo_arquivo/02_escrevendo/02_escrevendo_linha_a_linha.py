from pathlib import Path

# Escrevendo linha a linha
pasta_atual = Path(__file__).parent
itens_comprados = ['farinha', 'fermento', 'água']
with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()
itens_lista_atualizada = []
for item in itens_lista:
    if not item.replace('\n', '') in itens_comprados:
        itens_lista_atualizada.append(item)
with open(pasta_atual / 'lista_nova_atualizada.txt', mode='w') as lista_atualizada:
    itens_lista_atualizada[-1] = itens_lista_atualizada[-1].replace('\n', '')
    lista_atualizada.writelines(itens_lista_atualizada)
print(itens_lista)
print(itens_lista_atualizada)

