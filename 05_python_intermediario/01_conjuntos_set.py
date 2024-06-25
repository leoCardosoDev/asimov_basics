import timeit

# Set
a = {1, 2, 3, 4}
print(type(a))
b = set([3, 4, 5, 6, 7])
print(f'Conjunto A: {a}')
print(f'Conjunto B: {b}')
print()
# Não pode ter valor repetidos
c = {1, 2, 2, 2, 2, 1, 2, 1}
print(c)  # Remove os valores repetidos
# Adicionar valor
c.add(3)
print(c)
print()
# Exemplo de aplicação prática
numeros = [1, 2, 3, 2, 1, 4, 5, 3, 2, 1, 2]
print(f'Números totais: {numeros}')
numeros_unicos = list(set(numeros))
print(f'Números únicos: {numeros_unicos}')
print()
# Aceitam qualquer tipo de dados e não dá para definir uma ordem
d = {10, 'Python', 'python', 1.0, False}
print(f'Conjunto D: {d}')
# print(d[0]) # TypeError: 'set' object is not subscriptable
for elemnto in d:
    print(f'Conjunto D: {elemnto}')
# Não pode conter objetos mutáveis
# e = {1, 2, 3, [4, 5, 6]}
# print(e) # TypeError: unhashable type: 'list'
print()
# Tuplas podem ser usadas
e = {(1, 2, 3), (4, 5, 6)}
print(f'Conjunt E: {e}')

print()
# União de conjuntos
print(f'União de A e B: {a.union(b)}')
print(f'União de A e B: {a | b}')
print()
# Intersecção de conjuntos
print(f'Intersecção de conjuntos A e B: {a.intersection(b)}')
print(f'Intersecção de conjuntos A e B: {a & b}')
print()
# Diferença de conjuntos
# A para B
print(f'Diferença de conjuntos de A para B: {a.difference(b)}')
print(f'Diferença de conjuntos de A para B: {a - b}')
# B para A
print(f'Diferença de conjuntos de B para A: {b.difference(a)}')
print(f'Diferença de conjuntos de B para A: {b - a}')
print()
# Diferença simetrica
print(f'Diferença simetrica de conjuntos A para B: {a.symmetric_difference(b)}')
print(f'Diferença simetrica de conjuntos A para B: {(a - b) | (b - a)}')
print()

