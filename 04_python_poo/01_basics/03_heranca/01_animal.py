class Animal:
    def __init__(self):
        print("Animal criado")

    def quem_sou_eu(self):
        print("Eu sou um animal!")

    def comer(self):
        print("Eu te comi")


class Dog(Animal):
    def __init__(self):
        print("Cachorro criado")

    def quem_sou_eu(self):
        print('Eu sou um cachorro!')


animal = Animal()
dog = Dog()

animal.quem_sou_eu()
dog.quem_sou_eu()
