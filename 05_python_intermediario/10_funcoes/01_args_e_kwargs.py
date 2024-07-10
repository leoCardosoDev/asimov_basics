# Argumentos arbitrários co *args e *kwargs
def somar_fixo(a, b, c):
    return a+b+c
print(somar_fixo(1,2,3))

def somar_com_args(*valores, **valores2):
    return sum(valores)
print(somar_com_args(1,2,3,4,5, x=6, y=7))
