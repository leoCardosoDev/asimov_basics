from pathlib import Path
import os

# Retornando caminho do diretório de trabalho atual
print(Path.cwd())

# Esse é caminho absoluto!
print(Path.cwd().is_absolute())
