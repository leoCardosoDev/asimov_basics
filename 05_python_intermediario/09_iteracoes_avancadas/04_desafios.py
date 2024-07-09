"""
Desafio 01
Crie uma função que retorna os valores de duas listas de forma intercalada, mesmo quando as listas têm tamanho diferente. 
Por exemplo, dadas as listas:
L1 = [1, 2, 3]
L2 = ['a', 'b', 'c', 'd', 'e']
A função deve retornar:
[1, 'a', 2, 'b', 3, 'c', 'd', 'e']

Desafio 02
Imagine que você tem um restaurante com os seguintes itens no seu menu:
comidas = {
    'Prato Feito': 24.90,
    'Salada': 21.90,
    'Strogonoff': 29.90,
    'Feijoada': 32.90,
}
bebidas = {
    'Água': 3.90,
    'Refrigerante': 5.90,
    'Suco': 7.90,
}
Crie um novo dicionário chamado combos onde cada chave é uma 
tupla contendo (comida, bebida), e o seu respectivo valor é o preço daquela combinação de comida e bebida.
"""
import itertools


def retorna_intercalados(lista1, lista2):
    resultado = []
    for valor1, valor2 in itertools.zip_longest(lista1, lista2):
        if valor1 is not None:
            resultado.append(valor1)
        if valor2 is not None:
            resultado.append(valor2)
    return resultado

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c', 'd', 'e']

print(retorna_intercalados(lista1, lista2))
print()
print('***' * 50)
print()

# Desafio otmizado
def intercalar_listas(lista1, lista2):
    return [item for pair in itertools.zip_longest(lista1, lista2) for item in pair if item is not None]

# Exemplos
L1 = [4, 5, 6]
L2 = ['f', 'g', 'h', 'i', 'j']
resultado = intercalar_listas(L1, L2)
print(resultado)  # Saída: [1, 'a', 2, 'b', 3, 'c', 'd', 'e']
print()
print('***' * 50)
print()
# Desafio 2
comidas = {
    'Prato Feito': 24.90,
    'Salada': 21.90,
    'Strogonoff': 29.90,
    'Feijoada': 32.90,
}
bebidas = {
    'Água': 3.90,
    'Refrigerante': 5.90,
    'Suco': 7.90,
}
# Maneira tradicional
combo1 = {}
for chave_comida_t, preco_comida_t in comidas.items():
    for chave_bebida_t, preco_bebida_t in bebidas.items():
        chave_combo_t = (chave_comida_t, chave_bebida_t)
        preco_combo_t = preco_comida_t + preco_bebida_t
        combo1[chave_combo_t] = round(preco_combo_t, 2)
print(combo1)
print()
print('***' * 50)
print()
# itertools way
combo = {}
for chave_combo in itertools.product(comidas, bebidas):
    chave_comida, chave_bebida = chave_combo
    preco_combo = comidas[chave_comida] + bebidas[chave_bebida]
    combo[chave_combo] = round(preco_combo, 2)
print(combo)
print()
print('***' * 50)
print()