import json
import sys


sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

data_json = '''
{
  "assinantes" : [
    {
      "nome": "Adriano Soares",
      "telefone": "51 99999999",
      "email": "adriano@email.com",
      "em_dia": true
    },
    {
      "nome": "Juliano faccioni",
      "telefone": "51 99999999",
      "email": "juliano@email.com",
      "em_dia": false
    }
    ],
  "data_extração": "2023/08/22"
}
'''

print(type(data_json))
dado_convertido = json.loads(data_json)
print(type(dado_convertido))

# Convertendo dicionario para json com identação
dict_para_json = json.dumps(dado_convertido, ensure_ascii=False, indent=2)
print(type(dict_para_json))
print(dict_para_json)
