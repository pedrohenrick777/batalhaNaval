from tabuleiros import tabuleiro, frotas
from printjg import printTeste, printJogo, limpar_tela
from tiro import resul_tiro, tiro
import time


def novoJogo():
    limpar_tela()

    #Pergunta a quantidade de navios que vai ser usado e valida a resposta
    while True:
        quantNavios = int(
            input('Digite a quantidade de navios de cada jogador [Máx = 10]: '))
        if quantNavios < 0 or quantNavios > 10:
            print('ERRO')
            time.sleep(1)
            continue
        else:
            break
    
    #Cria o tabuleiro de frotas do jogador 1
    tabuP1 = tabuleiro()
    tabuP1 = frotas(tabuP1, quantNavios)
    #Cria o tabuleiro de frotas do jogador 2
    tabuP2 = tabuleiro()
    tabuP2 = frotas(tabuP2, quantNavios)
    #Cria o tabuleiro que vai ser exibido para os jogadores
    tabuP11 = tabuleiro()
    tabuP22 = tabuleiro()
    #Pontuação dos jogadores 1 e 2
    pontuacaoP1 = 0
    pontuacaoP2 = 0
    #Contagem para indicar de quem a vez de jogada, onde (Ímpar = Jogador 1) e (PAR = Jogador 2) 
    cont = 1
    #Opção de para ativar a exibição do tabuleiro de frotas dos usuários (APENAS PARA TESTE)
    teste = input(
        'Deseja mostrar as frotas(Função de Teste)?[Sim ou Não] ').upper()

    while True:
        #Valida se deve ser exibido o tabuleiro de frotas ou não
        if teste == 'SIM':
            printJogo(tabuP11, tabuP22, pontuacaoP1, pontuacaoP2)
            printTeste(tabuP1, tabuP2)
        else:
            printJogo(tabuP11, tabuP22, pontuacaoP1, pontuacaoP2)
        print()

        #Testa se algum dos jogadores já ganhou a partida
        if pontuacaoP1 == quantNavios:
            print('JOGADOR 1 GANHOU!!')
            time.sleep(10)
            break
        elif pontuacaoP2 == quantNavios:
            print('JOGADOR 2 GANHOU!!')
            time.sleep(10)
            break
        
        #Verifica de quem é a vez de jogada
        if cont % 2 != 0:
            print('-Jogador 1-')
            
            #Pega qual linha e coluna o jogador escolheu para atacar
            linha, coluna = tiro()

            #Verifica se o jogador acertou um navio
            if resul_tiro(tabuP2, tabuP22, linha, coluna):
                pontuacaoP1 += 1
            else:
                cont += 1
        else:
            print('-Jogador 2-')

            #Pega qual linha e coluna o jogador escolheu para atacar
            linha, coluna = tiro()

            #Verifica se o jogador acertou um navio
            if resul_tiro(tabuP1, tabuP11, linha, coluna):
                pontuacaoP2 += 1
            else:
                cont += 1



