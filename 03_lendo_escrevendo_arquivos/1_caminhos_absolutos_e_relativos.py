from pathlib import Path

caminho_atual = Path.cwd()
caminho_errado = Path('primeira_pasta').exists()
caminho_certo = Path('03_lendo_escrevendo_arquivos/assets/primeira_pasta').exists()

print(caminho_atual)
print(caminho_errado)
print()
print(caminho_certo)
