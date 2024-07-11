# utilidades do módulo functools
import functools
# Quando isso é útil com exemplo prático?
@functools.cache
def fatorial(n):
    print(f'Valor de n {n}')
    if n == 1:
        return n
    return n * fatorial(n-1)
print(fatorial(4))
print(fatorial(4))

def somar(a, b):
    return a+b

somar_dois = functools.partial(somar, 2)
print(somar(1, 2))
print(somar_dois(3))