# Argumentos arbitrários co *args e *kwargs
def somar_fixo(a, b, c):
    return a+b+c
print(somar_fixo(1,2,3))

def somar_com_args(*valores, **valores2):
    return sum(valores)
print(somar_com_args(1,2,3,4,5, x=6, y=7))

# Convenção
def exibir_argumentos(*args, **kwargs):
    print(f'Argumentos passados SEM palavra-chave: {args}')
    print(f'Argumentos passados COM palavra-chave: {kwargs}')
exibir_argumentos('a,', 'b', 'c', 1, 2, 3, a='A', b='B', c='C')

# Desempacotando argumentos
valores = [2, 4, 6, 8]
dicionario = { 'nome': 'Leonardo', 'idade': 42, 'cpf': 'xxx.xxx.xxx-xx'}
def desempactando_variaveis(*args, **kwargs):
    print('---'*30)
    print(args)
    print(kwargs)
    print('---'*30)
desempactando_variaveis(*valores, **dicionario)

def registrar_mensagem(nivel, *mensagens, **detalhes):
    print(f"Nível: {nivel}")
    for mensagem in mensagens:
        print(f"Mensagem: {mensagem}")
    for chave, valor in detalhes.items():
        print(f"{chave}: {valor}")

registrar_mensagem('INFO', 'Iniciando o sistema', 'Conexão estabelecida', usuario='admin', tempo='12:00')
