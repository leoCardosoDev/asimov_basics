# is instance
valor1 = 2.5
if isinstance(valor1, (int, float)):
    print('Valor é do tipo númerico')
else:
    print('Valor não é do tipo númerico')

# any e all
booleanos = [True, False, True]
print(all(booleanos))
print(any(booleanos))
valores = [1, 2, 2.5, 3]
if all(isinstance(valor, int) for valor in valores):
    print('Todos os valores são int')
else:
    print('Nem todos os valores são int')