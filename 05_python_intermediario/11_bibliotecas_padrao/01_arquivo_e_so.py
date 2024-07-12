# Interação com arquivos do sistema operacional
import os
print(os.getcwd())
print(os.listdir())
print(os.environ)
print('####'*35)
print()
print(os.environ['PATH'])

from pathlib import Path
p = Path('.')
print(p.absolute)