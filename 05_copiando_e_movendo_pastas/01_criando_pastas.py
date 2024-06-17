from pathlib import Path

# Criando pastas
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'assets/destino/04'
# caminho_pasta_destino.mkdir(exist_ok=True)
caminho_pasta_destino.mkdir(exist_ok=True, parents=True)
print(pasta_atual)
