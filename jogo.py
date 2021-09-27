from tabuleiros import boards, fleets
from printjg import print_test, print_game, clean_screen
from tiro import result_shot, shot
import time

#{{Pedro H.}}
def new_game():
    clean_screen()

    #Pergunta a quantidade de navios que vai ser usado e valida a resposta
    while True:
        numberShips = int(
            input('Digite a quantidade de navios de cada jogador [Máx = 10]: '))
        if numberShips <= 0 or numberShips > 10:
            print('ERRO')
            time.sleep(1)
            continue
        else:
            break
    
    #Cria o tabuleiro de frotas do jogador 1
    boardTP1 = boards()
    boardTP1 = fleets(boardTP1, numberShips)
    #Cria o tabuleiro de frotas do jogador 2
    boardTP2 = boards()
    boardTP2 = fleets(boardTP2, numberShips)
    #Cria o tabuleiro que vai ser exibido para os jogadores
    boardP1 = boards()
    boardP2 = boards()
    #Pontuação dos jogadores 1 e 2
    scoreP1 = 0
    scoreP2 = 0
    #Contagem para indicar de quem a vez de jogada, onde (Ímpar = Jogador 1) e (PAR = Jogador 2) 
    count = 1
    #Opção de para ativar a exibição do tabuleiro de frotas dos usuários (APENAS PARA TESTE)
    test = input(
        'Deseja mostrar as frotas(Função de Teste)?[Sim ou Não] ').upper()

    while True:
        #Valida se deve ser exibido o tabuleiro de frotas ou não
        if test == 'SIM':
            print_game(boardP1, boardP2, scoreP1, scoreP2)
            print_test(boardTP1, boardTP2)
        else:
            print_game(boardP1, boardP2, scoreP1, scoreP2)
        print()

        #Testa se algum dos jogadores já ganhou a partida
        if scoreP1 == numberShips:
            print('JOGADOR 1 GANHOU!!')
            time.sleep(10)
            break
        elif scoreP2 == numberShips:
            print('JOGADOR 2 GANHOU!!')
            time.sleep(10)
            break
        
        #Verifica de quem é a vez de jogada
        if count % 2 != 0:
            print('-Jogador 1-')
            
            #Pega qual linha e coluna o jogador escolheu para atacar
            line, column = shot()

            #Verifica se o jogador acertou um navio
            if result_shot(boardTP2, boardP2, line, column):
                scoreP1 += 1
            else:
                count += 1
        else:
            print('-Jogador 2-')

            #Pega qual linha e coluna o jogador escolheu para atacar
            line, column = shot()

            #Verifica se o jogador acertou um navio
            if result_shot(boardTP1, boardP1, line, column):
                scoreP2 += 1
            else:
                count += 1



