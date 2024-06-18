from pathlib import Path

# Lendo linha a linha
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    linha = lista_compras.readline()
    while linha != '':
        print(linha, end='')
        linha = lista_compras.readline()
