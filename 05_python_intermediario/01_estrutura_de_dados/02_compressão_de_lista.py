# Compreensão de lista

valores = list(range(15))
# Primeira maneira
'''
nova_lista = []
para cada ELEMENTO em SEQUÊNCIA
  se CONDIÇÃO:
    RESULTADO entra em nova_lista
'''
lista = []
for valor in valores:
  if valor > 5:
    lista.append(valor)
print(valores)
print(lista)

# Sengunda maneira: Compreensão de listas
## nova_lista = [RESULTADO para casa ELEMENTO em SEQUÊNCIA se CONDIÇÃO]
nova_lista = [valor for valor in valores if valor > 5]
print(nova_lista)

def somar_dois_ao_quadrado(valor):
  return (valor ** 2) + 2

maiores_que_cinco = [somar_dois_ao_quadrado(valor) for valor in valores if valor > 5]
print(maiores_que_cinco)
