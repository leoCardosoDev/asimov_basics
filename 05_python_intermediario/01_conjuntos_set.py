# Set
a = {1, 2, 3, 4}
print(type(a))
b = set([3, 4, 5, 6, 7])
print(f'Conjunto A: {a}')
print(f'Conjunto B: {b}')
# Não pode ter valor repetidos
c = {1, 2, 2, 2, 2, 1, 2, 1}
print(c)  # Remove os valores repetidos
# Adicionar valor
c.add(3)
print(c)
# Exemplo de aplicação prática
numeros = [1, 2, 3, 2, 1, 4, 5, 3, 2, 1, 2]
print(f'Números totais: {numeros}')
numeros_unicos = list(set(numeros))
print(f'Números únicos: {numeros_unicos}')
# Aceitam qualquer tipo de dados e não dá para definir uma ordem
d = {10, 'Python', 'python', 1.0, False}
print(f'Conjunto D: {d}')
# print(d[0]) # TypeError: 'set' object is not subscriptable
for elemnto in d:
    print(f'Conjunto D: {elemnto}')
# Não pode conter objetos mutáveis
# e = {1, 2, 3, [4, 5, 6]}
# print(e) # TypeError: unhashable type: 'list'
# Tuplas podem ser usadas
e = {(1, 2, 3), (4, 5, 6)}
print(f'Conjunt E: {e}')

# União de conjuntos
print(f'União de A e B: {a.union(b)}')
print(f'União de A e B: {a | b}')

