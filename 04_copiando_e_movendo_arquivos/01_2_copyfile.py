from pathlib import Path
import shutil

# Copiando arquivo com copy
pasta_atual = Path(__file__).parent
print(pasta_atual)
caminho_arquivo_origem = pasta_atual / 'assets' / 'texto.txt'
print(caminho_arquivo_origem)
caminho_pasta_destino = pasta_atual / 'assets/destino/02'
shutil.copy(caminho_arquivo_origem, caminho_pasta_destino)
