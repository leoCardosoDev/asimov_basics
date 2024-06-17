from pathlib import Path
import os

# Retornando caminho do diretório de trabalho atual
print(Path.cwd())

# Esse é caminho absoluto!
print(Path.cwd().is_absolute())

# Retornando caminho da primeira pasta
print(Path('03_lendo_escrevendo_arquivos/assets/primeira_pasta'))
# Esse é caminho absoluto?
print(Path('03_lendo_escrevendo_arquivos/assets/primeira_pasta').is_absolute())

# Transformando o caminho em absoluto
print(Path.cwd() / '03_lendo_escrevendo_arquivos/assets/primeira_pasta')
print((Path.cwd() / '03_lendo_escrevendo_arquivos/assets/primeira_pasta').exists())
# Trocando de pasta
os.chdir(Path.home())
print(Path.cwd() / '03_lendo_escrevendo_arquivos/assets/primeira_pasta')
print((Path.cwd() / '03_lendo_escrevendo_arquivos/assets/primeira_pasta').exists())

# Garantindo que estamos retornando o caminho para a pasta do script
print(__file__)
print(Path(__file__))
print(Path(__file__).is_absolute())
print(Path(__file__).parent)
print(Path(__file__).parent / 'assets/primeira_pasta')
print((Path(__file__).parent / 'assets/primeira_pasta').exists())
print('\n\n')
# Trabalhando com partes de caminho
caminho_arquivo = Path(__file__)
print('Pasta Atual')
print(caminho_arquivo)  # pasta atual
print('================================ \n')

print('Pasta Raiz')
print(caminho_arquivo.anchor)  # pasta raiz
print('================================\n')

print('Pasta Anterior')
print(caminho_arquivo.parent)  # pasta anterior
print('================================\n')

print('Tipo de caminho (Sistema operacional)')
print(type(caminho_arquivo.parent))  # tipo
print('================================\n')

print('Nome do arquivo COM extensão')
print(caminho_arquivo.name)  # nome
print('================================\n')

print('Nome do arquivo SEM extensão')
print(caminho_arquivo.stem)  # nome
print('================================\n')

print('Obtendo a extensão do arquivo')
print(caminho_arquivo.suffix)  # extensão do arquivo
print('================================\n')

print('Nome do disco no Computador')
print(caminho_arquivo.drive)  # Nome do disco
print('================================\n')

print('Diferença de PARENT e PARENTS')
print(caminho_arquivo.parent)  # pasta anterior
print(caminho_arquivo.parent.parent)  # Modo de acessar a pasta anterior da anterior
print(caminho_arquivo.parents[0])  # Modo de acessar as pastas anteriores mais rápido
print(caminho_arquivo.parents[1])  # Modo de acessar as pastas anteriores mais rápido
print(caminho_arquivo.parents[2])  # Modo de acessar as pastas anteriores mais rápido
print(caminho_arquivo.parents[3])  # Modo de acessar as pastas anteriores mais rápido
print(len(caminho_arquivo.parents))
print('================================\n')
