import os

carros = [
    ('Chevrolet Tracker', 120),
    ('Chevrolet Onix', 90),
    ('Chevrolet Spin', 150),
    ('Hyundai HB20', 85),
    ('Chevrolet Tucson', 120),
    ('Fiat Uno', 60),
    ('Fiat Mobi', 70),
    ('Fiat Pulse', 130),
]
alugados = []


def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} por dia.".format(i, car[0], car[1]))


while True:
    os.system('clear')
    print("================================")
    print("Bem-vindo a Locadora de carros")
    print("================================")
    print('')
    print("O que deseja fazer?")
    print("\n 0 - Mostrar portifólio\n 1 - Alugar um carro \n 2 - Devolver um carro")
    op = int(input())
    if op == 0:
        mostrar_lista_de_carros(carros)
    elif op == 1:
        mostrar_lista_de_carros(carros)
        print("================================================================")
        print("Escolha o código do carro:")
        cod_car = int(input())
        print('Por quantos dias quer alugar?')
        dias = int(input())
        os.system("clear")
        print("Você escolheu {} por {} dia(s).".format(
            carros[cod_car][0], dias))
        print("O aluguel totalizaria R$ {}. Deseja alugar?".format(dias * carros[cod_car][1]))
        print("S - SIM | N - NÃO")
        conf = input()
        if conf == 's':
            print('Parabéns! Você alugou o {} por {} dia(s).'.format(
                carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))
    elif op == 2:
        if (len(alugados)) == 0:
            print('Não há carros para devolver.')
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            mostrar_lista_de_carros(alugados)
            print('Escolha o código do carro que deseja devolver:')
            cod = int(input())
            if conf == 's':
                print("Obrigado por devolver o carro {}". format(
                    alugados[cod][0]))
                carros.append(alugados.pop(cod))
    print("")
    print("Quer continuar? 'S' para sim ou 'N' para não")
    if input() == 'n':
        break
