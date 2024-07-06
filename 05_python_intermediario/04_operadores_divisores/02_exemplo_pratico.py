segundos_totais = 10000

# Calcula o número total de horas
horas = segundos_totais // 3600
print(horas)  # Saída: 2

# Calcula o restante após as horas
resto = segundos_totais % 3600

# Calcula o número total de minutos
minutos = resto // 60
print(minutos)  # Saída: 46

# Calcula o restante após os minutos
segundos = resto % 60
print(segundos)  # Saída: 40

# Exibe o resultado formatado
print(f'{horas}h{minutos}m{segundos}s')  # Saída: 2h46m40s