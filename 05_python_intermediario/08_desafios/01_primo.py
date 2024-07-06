# Desafio 01
# Crie uma função que retorna se um número inteiro n maior que zero é primo
# Dica: um número primo é um número que só é divisivel por um ou por ele mesmo
def primo(n):
    if n <= 1:
        return False  # Corrigido para retornar False se n <= 1
    if n == 2:
        return True  # 2 é um número primo
    for divisor in range(2, int(n**0.5) + 1):  # Verificação otimizada até a raiz quadrada de n
        if n % divisor == 0:
            return False
    return True

for n in [1, 5, 10, 13, 15, 17]:
    print(f'Número {n} é primo? {primo(n)}')