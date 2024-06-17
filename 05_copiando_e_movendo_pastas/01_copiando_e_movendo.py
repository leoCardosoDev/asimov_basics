from pathlib import Path
import shutil

# Copiando arquivo com copyfile
pasta_atual = Path(__file__).parent
print(pasta_atual)
caminho_arquivo_origem = pasta_atual / 'assets' / 'texto.txt'
print(caminho_arquivo_origem)
caminho_arquivo_destino = pasta_atual / 'assets/destino/01' / 'texto.txt'
# Garantir que o diretório de destino exista
# caminho_arquivo_destino.parent.mkdir(parents=True, exist_ok=True)
# Copiar o arquivo
shutil.copyfile(caminho_arquivo_origem, caminho_arquivo_destino)


# Copiando arquivo com copy
pasta_atual = Path(__file__).parent
print(pasta_atual)
caminho_arquivo_origem = pasta_atual / 'assets' / 'texto.txt'
print(caminho_arquivo_origem)
caminho_arquivo_destino = pasta_atual / 'assets/destino/01' / 'texto.txt'
# Garantir que o diretório de destino exista
# caminho_arquivo_destino.parent.mkdir(parents=True, exist_ok=True)
# Copiar o arquivo
shutil.copyfile(caminho_arquivo_origem, caminho_arquivo_destino)
# Copiando arquivo com copy2

# Movendo arquivos
# Deletando arquivos
