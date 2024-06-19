import pickle
from pathlib import Path

# Salvando arquivos pickle
minha_lista = [0, 1, 2]
meu_dict = {'a':1, 'b': 'dois', '3': True}
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'pickles' / 'minha_lista.pickle', 'wb') as lista:
  pickle.dump(minha_lista, lista)

with open(pasta_atual / 'pickles' / 'meu_dict.pickle', 'wb') as dict:
  pickle.dump(meu_dict, dict)
