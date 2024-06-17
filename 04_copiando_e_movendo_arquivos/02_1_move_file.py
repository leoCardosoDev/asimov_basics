from pathlib import Path
import shutil

# Movendo arquivos
pasta_atual = Path(__file__).parent
print(pasta_atual)
caminho_arquivo_origem = pasta_atual / 'assets' / 'move.txt'
print(caminho_arquivo_origem)
caminho_pasta_destino = pasta_atual / 'assets/destino/01'
shutil.move(caminho_arquivo_origem, caminho_pasta_destino)
