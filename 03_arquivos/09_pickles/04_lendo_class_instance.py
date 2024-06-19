import pickle
from pathlib import Path

# Lendo a instancia de uma classe
pasta_atual = Path(__file__).parent


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def quem_sou_eu(self):
        print(f'Eu sou {self.nome} e tenho {self.idade} anos.')


with open(pasta_atual / 'pickles' / 'inst_pessoa.pickles', 'rb') as f:
    inst_pickles = pickle.load(f)

inst_pickles.quem_sou_eu()
