from pathlib import Path

# Criando pastas
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'assets/destino/04'
caminho_pasta_destino.mkdir(parents=True, exist_ok=True)
print(pasta_atual)
