# Lambdas
def meu_filtro(x):
    return x > 2

filtro_sem_lambda = filter(meu_filtro, [1, 2, 3, 4, 5, 6])
print(list(filtro_sem_lambda))

filtro = filter(lambda x: x > 2, [1, 2, 3, 4, 6])
print(list(filtro))