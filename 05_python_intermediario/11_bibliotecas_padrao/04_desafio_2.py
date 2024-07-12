def diff_tempo(tempo1, tempo2):
    # Dividir os tempos em horas, minutos e segundos
    h1, m1, s1 = map(int, tempo1.split(':'))
    h2, m2, s2 = map(int, tempo2.split(':'))
    
    # Calcular a diferença em segundos
    total_segundos1 = h1 * 3600 + m1 * 60 + s1
    total_segundos2 = h2 * 3600 + m2 * 60 + s2
    diff_segundos = abs(total_segundos1 - total_segundos2)
    
    # Calcular horas, minutos e segundos da diferença
    horas_diff = diff_segundos // 3600
    minutos_diff = (diff_segundos % 3600) // 60
    segundos_diff = diff_segundos % 60
    
    # Formatar a diferença de tempo de volta para o formato HH:MM:SS
    diff_formatado = '{:02}:{:02}:{:02}'.format(horas_diff, minutos_diff, segundos_diff)
    
    return diff_formatado

# Exemplo de uso da função
tempo1 = '10:15:30'
tempo2 = '12:45:15'

diferenca = diff_tempo(tempo1, tempo2)
print(f'A diferença de tempo entre {tempo1} e {tempo2} é {diferenca}')
