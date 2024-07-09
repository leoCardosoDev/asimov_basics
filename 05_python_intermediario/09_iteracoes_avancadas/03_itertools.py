import itertools

# chain
seq1 = (1, 2, 3)
seq2 = ['a', 'b', 'c']
for elemento in itertools.chain(seq1, seq2):
    print(elemento)