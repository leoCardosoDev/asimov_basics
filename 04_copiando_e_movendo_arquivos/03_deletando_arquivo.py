from pathlib import Path
import shutil
import os

# Removendo arquivo
pasta_atual = Path(__file__).parent
print(pasta_atual)
caminho_arquivo_origem = pasta_atual / 'assets' / 'file_deleted.txt'
print(caminho_arquivo_origem)
caminho_pasta_destino = pasta_atual / 'assets/destino/03/file_deleted.txt'
shutil.copyfile(caminho_arquivo_origem, caminho_pasta_destino)
os.remove(caminho_arquivo_origem)
