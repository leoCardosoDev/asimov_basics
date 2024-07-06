# Modo verboso
arquivo = open('notas.txt', 'w')
arquivo.write('Esta é uma anotação especial!')
arquivo.close()

# com with
with open('notas.txt', 'w') as arquivo2:
    arquivo2.write('Nova linha de código')
print('Arquivo foi fechado')