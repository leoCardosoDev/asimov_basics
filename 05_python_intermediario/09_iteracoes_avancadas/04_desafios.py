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