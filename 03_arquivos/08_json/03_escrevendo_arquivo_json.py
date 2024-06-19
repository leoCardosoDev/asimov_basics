import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Escrevendo arquivos Json
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'jsons' / 'assinantes.json') as f:
  dado_carregado = json.load(f)

with open(pasta_atual / 'jsons' / 'assinantes_copia.json', mode='w') as f:
  json.dump(dado_carregado, f, indent=2, ensure_ascii=False)
