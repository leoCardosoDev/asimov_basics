import xml.dom.minidom
from pathlib import Path

# Lendo Arquivo xml
pasta_atual = Path(__file__).parent
domtree = xml.dom.minidom.parse(str(pasta_atual / 'xmls' / 'livros.xml'))
group = domtree.documentElement
livros = domtree.getElementsByTagName('livro')

# Interando pelos nodes xml
for livro in livros:
  titulo = livro.getElementsByTagName('titulo')[0].childNodes[0].nodeValue
  autor = livro.getElementsByTagName('autor')[0].childNodes[0].nodeValue
  preco = livro.getElementsByTagName('preco')[0].childNodes[0].nodeValue
  print('Titulo:', titulo, '\nAutor:',  autor, '\nR$', preco)
  print()
