# Enummerate
nomes = ['Juliano', 'José', 'Lucas', 'Luiza']
for i, nome in enumerate(nomes, 1):
    print(f'Indice: {i} -> Nome: {nome}')

# Sorted
conjunto = [10, 4, 0, 5, 9, 1, -1, -2]
ordenados = sorted(conjunto)
ordenados_reversed = sorted(conjunto, reverse=True)
print(f'Conjunto: {conjunto}\nOrdenados: {ordenados}')
print()
print(f'Ordenados: {ordenados}\nOrdenados reverso: {ordenados_reversed}')

# Reversed
for i in reversed(range(10)):
    print(i)

# zip
new_names = ['Leo', 'Pri', 'Laura', 'Roberto', 'Guilherme']
idades = [42, 34, 19, 47, 22]
for elemento in zip(new_names, idades):
    print(elemento)
