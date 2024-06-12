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
