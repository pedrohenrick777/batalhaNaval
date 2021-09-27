from printjg import limpar_tela
from jogo import novoJogo
import time


while True:
    #limpar terminal
    limpar_tela()

    print('''
        Novo Jogo[1]
        Fechar [2]
    ''')
    #Inicia um novo jogo ou fecha o jogo
    nv = int(input(''))
    if nv == 1:
        novoJogo()
    elif nv == 2:
        print('Programa Encerrado')
        break
    else:
        #caso seja digitado um número inválido
        print('Erro')
        #espera 1 seg
        time.sleep(1)
