from pathlib import Path

caminho_relativo = Path('assets/primeira_pasta/segunda_pasta')
caminho_absoluto = Path('/home/leoca/cursos/python/00_asimov/00_trilha_basics/03_lendo_escrevendo_arquivos/assets/primeira_pasta/segunda_pasta')
arquivo = ['arq1.txt', 'arq2.txt', 'arq3.txt']
home = Path.home()

for nome in arquivo:
    caminho_arquivo = caminho_relativo/nome
    print(caminho_arquivo)

print('\n================================')
print(home)
