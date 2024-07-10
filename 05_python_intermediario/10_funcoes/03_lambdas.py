# Lambdas
def meu_filtro(x):
    return x > 2

filtro_sem_lambda = filter(meu_filtro, [1, 2, 3, 4, 5, 6])
print(list(filtro_sem_lambda))

filtro = filter(lambda x: x > 2, [1, 2, 3, 4, 6])
print(list(filtro))
# Sintaxe da função lambda
# lambda <ARGUMENTO DA FUNÇÃO>: <LÓGICA DA FUNÇÃO>
# lambda x, y, z: x + y + z

# another example
mapa = map(lambda x: str(x+2), [1, 2, 3])
print(list(mapa))

print(list(map(lambda x: str(x+2), [1, 2, 3])))
