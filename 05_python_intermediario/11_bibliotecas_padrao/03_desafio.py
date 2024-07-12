import re
from datetime import datetime

def ler_datas(texto):
    # Padrão para encontrar datas no formato DD/MM/AAAA
    padrao_data = r'\b(\d{2})/(\d{2})/(\d{4})\b'
    
    # Lista para armazenar as datas encontradas
    datas = []
    
    # Encontrar todas as correspondências no texto
    for match in re.finditer(padrao_data, texto):
        dia = int(match.group(1))
        mes = int(match.group(2))
        ano = int(match.group(3))
        
        # Criar objeto datetime com a data encontrada
        data = datetime(ano, mes, dia)
        
        # Adicionar a data à lista
        datas.append(data)
    
    return datas

# Exemplo de uso da função com o texto fornecido
texto = """A reunião está marcada para o dia 15/03/2023.
Lembre-se de entregar o relatório até dia 28/02/2023.
O evento acontecerá em 10/04/2023 no auditório principal"""

datas_encontradas = ler_datas(texto)
for data in datas_encontradas:
    print(data)
