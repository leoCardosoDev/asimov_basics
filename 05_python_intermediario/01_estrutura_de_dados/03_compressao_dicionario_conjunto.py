valores = list(range(10))
# Tranformando em Set
maiores_que_cinco = {valor for valor in valores if valor > 5}
print(type(maiores_que_cinco))
print(maiores_que_cinco)

# Tranformando em Dicionario
ditc_maior_que_cinco = {valor: valor+2 for valor in valores if valor}
print(type(ditc_maior_que_cinco))
print(ditc_maior_que_cinco)

# Exemplo prático
valores_em_dolares = {
  'leite': 0.78,
  'carne': 4.60,
  'maçã': 0.35
}
fator_conversao = 4.95
valores_em_reais = { chave: round(valor * fator_conversao) for chave, valor in valores_em_dolares.items()}
print(valores_em_dolares)
print(valores_em_reais)
