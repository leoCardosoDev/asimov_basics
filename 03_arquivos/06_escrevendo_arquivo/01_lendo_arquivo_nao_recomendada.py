from pathlib import Path

# Lendo um arquivo (Forma não recomendada)
pasta_atual = Path(__file__).parent
lista_compras = open(pasta_atual / 'lista_de_compras.txt')
print(lista_compras.read())
lista_compras.close()
