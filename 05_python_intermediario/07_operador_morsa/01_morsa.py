# operador morsa :=
valor_de_busca = 'xxx'
# result = buscar_no_banco_de_dados(valor_de_busca)
result = 0
if result is None:
    print(f'Nada foi encontrado para o valor de busca "{valor_de_busca}"')
else:
    print(f'Resultados encontrados para valor de busca "{valor_de_busca}": {result}')

#if (resultado := buscar_no_banco_de_dados(valor_de_busca)) is None:
#    print(f'Nada foi encontrado para o valor de busca "{valor_de_busca}"')
#else:
#    print(f'Resultados encontrados para valor de busca "{valor_de_busca}": {resultado}')