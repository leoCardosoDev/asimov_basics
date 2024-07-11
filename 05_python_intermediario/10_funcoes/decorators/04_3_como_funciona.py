# Como decoradores funcionam?
# Criando um decorador
def meu_decorador(func):
    def meu_pacote(*args, **kwargs):
        retorno = func(*args, **kwargs)
        return retorno.upper()
    return meu_pacote

def dizer_oi(nome):
    return f'Olá {nome}!'

dizer_oi = meu_decorador(func=dizer_oi) # mesma cois que fazer @meu_decorador
print(dizer_oi('Pri Cardoso'))


