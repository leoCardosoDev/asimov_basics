from pathlib import Path
# Desenvolva um script para encontrar um arquivo dentro da pasta home do usuário
caminho = Path.home()
print(caminho)
for arquivo in caminho.glob('**/*'):
    if arquivo.is_file():
        # if arquivo.name == 'senha.txt':
        if arquivo.stem == 'senha':
            print(arquivo)
print('\n===============================================================\n')


def encontra_arquivo(caminho, nome_do_arquivo):
    for arquivo in caminho.glob('**/*'):
        if arquivo.is_file():
            if arquivo.stem == nome_do_arquivo:
                print(arquivo)


encontra_arquivo(Path.cwd(), 'senha')
