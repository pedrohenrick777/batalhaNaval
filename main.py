from jogo import novoJogo
import os
import time

while True:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print('''
        Novo Jogo[1]
        Fechar [2]
    ''')
    nv = int(input(''))
    if nv == 1:
        novoJogo()
    elif nv == 2:
        break
    else:
        print('Erro')
        time.sleep(1)
