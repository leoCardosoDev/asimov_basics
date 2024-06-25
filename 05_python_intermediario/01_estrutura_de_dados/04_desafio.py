# Exemplos de lista de palavras e o dicionario resultante

valores = [30, 50, 100, 120]
triplos = []
for valor in valores:
    triplo = valor * 3
    triplos.append(triplo)
print(triplos)

# Tranformando em compreensão de listas
tres = [triplo * 3 for triplo in valores]
print(tres)


# Transformando em dicionário adicionando chave e contando os caracteres
palavras = ['Olá', 'Python', 'Leo', 'Asimov Academy']
carater = {valor.lower(): len(valor.replace(' ', '')) for valor in palavras}
print(carater)
