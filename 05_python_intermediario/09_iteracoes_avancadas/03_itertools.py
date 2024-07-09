import itertools

# chain
seq1 = (1, 2, 3)
seq2 = ['a', 'b', 'c']
for elemento in itertools.chain(seq1, seq2):
    print(elemento)

# zip_longest
nomes = ['Leo', 'Pri', 'Laura', 'Roberto', 'Guilherme']
idades = [42, 34, 19, 47, 22]
cpfs = ['xxx', 'yyy', 'zzz']
emails = ['leo@gmail.com', 'pri@gmail.com']
for elemento in itertools.zip_longest(nomes, idades, cpfs, emails, fillvalue='???'):
    print(elemento)