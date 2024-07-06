op = 1
if op == 1:
    print('Opção 1')
elif op == 2:
    print('Opção 2')
else:
    print('Opção inválida')

match op:
    case int(op):
        print('É um inteiro')
    case str(op):
        print('É uma string')
    case _:
        print('Opção inválida')