# Decoradores existentes
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
