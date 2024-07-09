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
