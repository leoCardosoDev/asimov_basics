seq = (10, 20, 30)
a, b, c = seq
print('Sequência')
print(seq)
print('Desempacote')
print(a)
print(b)
print(c)

dic = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3',
}
for chave, valor in dic.items():
    print(chave, valor)

nomes = ['Leo', 'Pri', 'Laura', 'Roberto', 'Guilherme']
idades = [42, 34, 19, 47, 22]
for elemento in enumerate(zip(nomes, idades)):
    print(elemento)

for i, (nome, idade) in enumerate(zip(nomes, idades)):
    print(i, nome, idade)

minha_lista = [1, 2, 3, 4, 5]
primeiro, *meio, fim = minha_lista
print(primeiro)
print(meio)
print(fim)