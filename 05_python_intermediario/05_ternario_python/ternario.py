x = 4
y = 5
if x > y:
    maior_valor = x
else:
    maior_valor = y

print(maior_valor)

# Operador ternário em outras linguagens
# var CONDIÇÃO ? valor se VERDADEIRO : valor se FALSO

# Experssão condicional em Python
# var = valor_verdadeiro SE condição SENÃO valor_falso
x = 100
valor_maior = x if x > y else y
print(valor_maior)

def pega_cor(valor):
    return 'vermelho' if valor <= 0 else 'azul'

for valor in [-1, 0, 1, 2]:
    print(f'A cor do valor {valor} é {pega_cor(valor)}')

numeros = [1,2,3,4]
pares_quadrados = [ n** 2 if n % 2 == 0 else n for n in numeros]
print(f'Números: {numeros}')
print(f'Números ao quadrados de pares: {pares_quadrados}')