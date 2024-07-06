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

notas = {
    'João': 10,
    'Maria': 9,
    'Matheus': 9.5
}

match notas:
    case {'João': 10}:
        print('João tirou 10')
    case _:
        print('Nenhuma informação obtida!')

match notas:
    case {'Maria': _}:
        print('Maria está no dicionário!')
    case _:
        print('Nenhuma informação obtida!')