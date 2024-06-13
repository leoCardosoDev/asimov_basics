from pathlib import Path
import os

# Listando arquivos de uma pasta
print('LISTANDO ARQUIVOS DE UMA PASTA')
print(os.listdir(Path.cwd()))  # Listando com os
print(list(Path.cwd().glob('*')))
print('================================================================\n')
print(list(Path.cwd().glob('03_lendo_escrevendo_arquivos/')))
print('================================================================\n')
print(list(Path.cwd().glob('03_lendo_escrevendo_arquivos/*')))
print('================================================================\n')
print(list(Path.cwd().glob('03_lendo_escrevendo_arquivos/*.py')))

# Listando tudo dentro de uma pasta
print('================================================================\n')
print('LISTANDO TUDO')
print(list(Path.cwd().glob('03_lendo_escrevendo_arquivos/**/*')))
