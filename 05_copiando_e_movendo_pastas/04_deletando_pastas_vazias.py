from pathlib import Path

# Deletando pastas vazias
pasta_atual = Path(__file__).parent / 'assets' / 'destino'
pasta_remover = pasta_atual / '05' / '051'
pasta_remover.rmdir()
print(pasta_atual)
