import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Lendo arquivos Json
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'jsons' / 'assinantes.json') as f:
  dado_carregado = json.load(f)
  print(type(dado_carregado))
  print(dado_carregado)
  print()
  print(dado_carregado['assinantes'])
  print()
  print(dado_carregado['data_extração'])
