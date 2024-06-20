class Circle:
    def __init__(self, raio=1):
        self.raio = raio

    def clacula_area(self):
        return self.raio * self.raio * 3.14


circle1 = Circle()
circle2 = Circle(2)
print('Raio:')
print(circle1.raio)
print(circle2.raio)

print('Area calculada:')
print(circle1.clacula_area())
print(circle2.clacula_area())
