# Set

a = {1, 2, 3, 4} 
print(type(a))
b = set([3, 4, 5, 6, 7])
print(f'Conjunto A: {a}')
print(f'Conjunto B: {b}')
# Não pode ter valor repetidos
c = {1,2,2,2,2,1,2,1}
print(c) # Remove os valores repetidos
# Adicionar valor
c.add(3)
print(c)
# Exemplo de aplicação prática
numeros = [1, 2, 3, 2, 1, 4, 5, 3, 2, 1, 2]
print(f'Números totais: {numeros}')
numeros_unicos = list(set(numeros))
print(f'Números únicos: {numeros_unicos}')
