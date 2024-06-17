from pathlib import Path
import shutil

# Compactando arquivos
pasta_atual = Path(__file__).parent
pasta_a_ser_compactada = pasta_atual
nome_do_arquivo = pasta_atual / 'compactado'
shutil.make_archive(nome_do_arquivo, 'zip', pasta_a_ser_compactada)
# Descompactando arquivos
