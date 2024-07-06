lista_a = [1,2,3,4,5]
lista_b = [1,2,3,4,5]
print(lista_a == lista_b)
print(lista_a is lista_b)
lista_a.append(6)
print(lista_a == lista_b)

bolo1 = {
    'sabor': 'chocolate',
    'tamanho': 'grande',
    'preco': 50
}

bolo2 = {
    'sabor': 'chocolate',
    'tamanho': 'grande',
    'preco': 50
}
print(bolo1 == bolo2)
print(bolo1 is bolo2)
bolo1['preco'] == 80
print(bolo1 == bolo2)

print(True is True)
print(True is False)
print(False is True)
print(False is False)
print(None is None)

valor = 10
print('Valor é nulo' if valor is None else 'Valor não é nulo')