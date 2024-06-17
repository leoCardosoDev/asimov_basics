from pathlib import Path
import shutil

# Deletando pastas com conteúdo
pasta_atual = Path(__file__).parent / 'assets' / 'destino'
pasta_remover = pasta_atual / '04'
# pasta_remover.rmdir() # só funciona para pastas vazias
shutil.rmtree(pasta_remover)

