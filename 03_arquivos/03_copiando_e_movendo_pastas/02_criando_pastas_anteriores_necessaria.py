from pathlib import Path

# Criando pastas com todas as pastas anteriores necessárias
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'assets/destino/05' / '051'
caminho_pasta_destino.mkdir(parents=True, exist_ok=True)
print(pasta_atual)
