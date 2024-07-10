# is instance
valor1 = 2.5
if isinstance(valor1, (int, float)):
    print('Valor é do tipo númerico')
else:
    print('Valor não é do tipo númerico')

# any e all
booleanos = [True, False, True]
print(all(booleanos))