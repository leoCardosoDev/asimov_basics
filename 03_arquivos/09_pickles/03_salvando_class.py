import pickle
from pathlib import Path

# Salvando uma classe
pasta_atual = Path(__file__).parent

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def quem_sou_eu(self):
        print(f'Eu sou {self.nome} e tenho {self.idade} anos.')


inst_pessoa = Pessoa('Leo', 30)
inst_pessoa.quem_sou_eu()


with open(pasta_atual / 'pickles' / 'inst_pessoa.pickles', 'wb') as f:
    pickle.dump(inst_pessoa, f)
