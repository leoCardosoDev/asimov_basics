import xml.dom.minidom
from pathlib import Path

# Lendo Arquivo xml
pasta_atual = Path(__file__).parent
domtree = xml.dom.minidom.parse(str(pasta_atual / 'xmls' / 'livros.xml'))
group = domtree.documentElement
livros = domtree.getElementsByTagName('livro')
print(len(livros))
