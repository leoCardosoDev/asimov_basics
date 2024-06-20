class Dog:
  def __init__(self, raca):
    self.idade = 10
    self.raca = raca
    print(f'Cachorro {raca} instanciado')

dog = Dog('Lab')
dog2 = Dog('Chiuahua')

dog.idade = 12

print(dog.idade)
print(dog.raca)
print()
print(dog2.idade)
print(dog2.raca)
