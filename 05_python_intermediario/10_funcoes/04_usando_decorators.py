# Fundamentos antes de usar Decoradores
def funcao():
    return 3 + 1

minha_funcao = funcao
retorno = minha_funcao()
print(retorno)

def exibe_funcao(f):
    print(f'Objeto de função recebido: {f}')
    print(f'Nome da função: {f.__name__}')

exibe_funcao(funcao)
print('**'*40)

# Função dentro de função
def funcao_externa(x):
    def funcao_interna():
        return x + 2
    valor = funcao_interna()
    return valor

print(funcao_externa(3))

# Segundo exemplo
def func_externa(x):
    def func_interna(y):
        return x + y + 2
    valor = func_interna()
    return valor