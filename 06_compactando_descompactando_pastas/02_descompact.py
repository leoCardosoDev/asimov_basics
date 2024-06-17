from pathlib import Path
import shutil

# Descompactando arquivos
pasta_atual = Path(__file__).parent
nome_do_arquivo = pasta_atual / 'compactado.zip'
pasta_descompactada = pasta_atual / 'descompactado'
shutil.unpack_archive(nome_do_arquivo, pasta_descompactada, 'zip')
