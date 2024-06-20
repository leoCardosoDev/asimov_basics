class Dog:
    def __init__(self, raca):
        self.idade = 10
        self.raca = raca
        print(f'Cachorro {raca} instanciado')

    def envelhecer(self):
        self.idade += 1
        return self.idade


dog = Dog('Lab')
dog2 = Dog('Chiuahua')

dog.idade = 12
dog2.envelhecer()

print(dog.idade)
print(dog.raca)
print()
print(dog2.idade)
print(dog2.raca)
