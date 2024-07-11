# Com base no for loop abaixo
valores = [1, 2, 3, 5, 10]
quadrados_maiores_que_tres = []
for valor in valores:
    if valor > 3:
        quadrado = valor ** 2
        quadrados_maiores_que_tres.append(quadrado)

# Resolução
quadrados_maiores_que_tres = [valor ** 2 for valor in valores if valor > 3]
print(quadrados_maiores_que_tres)