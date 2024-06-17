from pathlib import Path
import shutil

# Copiando pastas
pasta_atual = Path(__file__).parent / 'assets' / 'destino'
shutil.copytree(pasta_atual  / '05', pasta_atual  / '04' / '05' )
print(pasta_atual)
