from meus_decoradores import fazer_duas_vezes, medir_tempo
import time

@medir_tempo
@fazer_duas_vezes
def printar_exclamacoes():
    print('!!!')
printar_exclamacoes()

@medir_tempo
@fazer_duas_vezes
def printar_tempo():
    time.sleep(2)
    print(time.localtime())
printar_tempo()