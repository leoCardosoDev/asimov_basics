import pickle
from pathlib import Path

# Lendo arquivos pickle
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'pickles' / 'minha_lista.pickle', 'rb') as lista:
    minha_lista_pickle = pickle.load(lista)

print(minha_lista_pickle)

with open(pasta_atual / 'pickles' / 'meu_dict.pickle', 'rb') as dict:
    meu_dict_pickle = pickle.load(dict)

print(meu_dict_pickle)
