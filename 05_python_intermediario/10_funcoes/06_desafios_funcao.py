valores = [1, 2, 3, 5, 10]

# Compreensão de Lista
quadrados_maiores_que_tres_comp = [valor ** 2 for valor in valores if valor > 3]
print("Compreensão de Lista:", quadrados_maiores_que_tres_comp)

# Usando map e filter
valores_maiores_que_tres = filter(lambda x: x > 3, valores)
quadrados = map(lambda x: x ** 2, valores_maiores_que_tres)
quadrados_maiores_que_tres_map_filter = list(quadrados)
print("map e filter:", quadrados_maiores_que_tres_map_filter)