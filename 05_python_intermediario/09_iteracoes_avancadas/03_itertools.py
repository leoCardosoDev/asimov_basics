import itertools

# chain
seq1 = (1, 2, 3)
seq2 = ['a', 'b', 'c']
for sequencia in itertools.chain(seq1, seq2):
    print(sequencia)

print()
print('***' * 50)
print()
# zip_longest
nomes = ['Leo', 'Pri', 'Laura', 'Roberto', 'Guilherme']
idades = [42, 34, 19, 47, 22]
cpfs = ['xxx', 'yyy', 'zzz']
emails = ['leo@gmail.com', 'pri@gmail.com']
for lista in itertools.zip_longest(nomes, idades, cpfs, emails, fillvalue='???'):
    print(lista)

print()
print('***' * 50)
print()
# product
comidas = ['Churrasco', 'Pizza', 'Sushi']
bebidas = ('Refrigerante', 'Água')
for prato in itertools.product(comidas, bebidas):
    print(prato)

print()
print('***' * 50)
print()
# combinations
names = ['Marcos', 'Lucas', 'Rodrigo', 'Carlos']
for combinacao in itertools.combinations(names, 2):
    print(combinacao)