from printjg import clean_screen
from jogo import new_game
import time

#{{Pedro H.}}
while True:
    #limpar terminal
    clean_screen()

    print('''
        Novo Jogo[1]
        Fechar [2]
    ''')
    #Inicia um novo jogo ou fecha o jogo
    newG = int(input(''))
    if newG == 1:
        new_game()
    elif newG == 2:
        print('Programa Encerrado')
        break
    else:
        #caso seja digitado um número inválido
        print('Erro')
        #espera 1 seg
        time.sleep(1)
