from pathlib import Path

def se_tiver_nomes_especificos(diretorio):
    return diretorio.is_dir() and not diretorio.name.startswith('.') and diretorio.name != 'node_modules'

def retorna_tamanho_arquivos(caminho, profundidade=1, tamanho_linha=0):
    for diretorio in caminho.glob('*'):
        if se_tiver_nomes_especificos(diretorio):
            tamanho_diretorio = sum(arquivo.stat().st_size for arquivo in diretorio.glob('**/*') if arquivo.is_file())
            print('--' * tamanho_linha, diretorio.name, round(tamanho_diretorio / 1024 / 1024, 2), 'MB')
            if profundidade > 1:
                retorna_tamanho_arquivos(diretorio, profundidade-1, tamanho_linha+1)

caminho = Path.home() / 'cursos'

retorna_tamanho_arquivos(caminho, profundidade=2)
