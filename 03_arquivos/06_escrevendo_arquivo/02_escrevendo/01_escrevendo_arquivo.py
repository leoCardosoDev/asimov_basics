from pathlib import Path

# Escrevendo arquivos
pasta_atual = Path(__file__).parent
itens_comprados = ['farinha', 'fermento', 'água']
with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()
with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode='w') as lista_atualizada:
    for item in itens_lista:
        if not item.replace('\n', '') in itens_comprados:
            lista_atualizada.write(item)
