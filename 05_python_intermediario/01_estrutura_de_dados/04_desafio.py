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

# Desafio 3
"""
  Meus amigos possuem os seguintes interesses
    1. Gostam de programação: Ricardo, Roberto, Pedro, Vinicius
    2. Gostam de jogar futebol: Matheus, Roberto, Paulo, Vinicius
    3. Estudam na Asimov Acaddemy: Ricardo, Matheus, Paulo, Pedro

  Usando operações de conjunto, encontre o conjunto de amigos que 
  gostam de programação e estudam na Asimov Acaddemy, mas que não 
  gostam de futebol
"""
gostam_de_programacao = {'Ricardo', 'Roberto', 'Pedro', 'Vinicius'}
gostam_futebol = {'Matheus', 'Roberto', 'Paulo', 'Vinicius'}
estudam_asimov = {'Ricardo', 'Matheus', 'Paulo', 'Pedro'}

result = gostam_de_programacao.intersection(
    estudam_asimov).difference(gostam_futebol)
print(result)
