from tabuleiros import tabuleiro, tabuleiro2
from printjg import printTeste, printJogo
import os
import time

def novoJogo():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    quantNavios = int(input('Digite a quantidade de navios de cada jogador [Máx = 10]: '))
    tabuP1 = tabuleiro(quantNavios)
    tabuP2 = tabuleiro(quantNavios)
    tabuP11 = tabuleiro2()
    tabuP22 = tabuleiro2()
    pontuacaoP1 = 0
    pontuacaoP2 = 0
    cont = 1
    abc = ['A','B','C','D','E','F','G','H','I','J']
    teste = input('Deseja mostrar as frotas(Função de Teste)?[S ou N] ').upper()

    while True:
        if teste == 'S':
            printTeste(abc, tabuP1, tabuP2, tabuP11, tabuP22)
        else:
            printJogo(abc, tabuP11, tabuP22)
        print()
        if cont%2 != 0:
            print('-Jogador 1-')
            linha = input('Qual linha do seu ataque? ').upper()
            coluna = int(input('Qual coluna do seu ataque? '))
            linha = ord(linha) - 65

            if tabuP22[linha][coluna-1] == 'F' or tabuP22[linha][coluna-1] == 'A':
                print('JÁ JOGADO - PERDEU A VEZ')
                cont += 1
                time.sleep(2)
            elif tiro(tabuP2, linha, coluna):
                tabuP22[linha][coluna-1] = 'F'
                print('FOGO - SUA VEZ NOVAMENTE')
                pontuacaoP1 += 1
                time.sleep(2)
            else:
                tabuP22[linha][coluna-1] = 'A'
                print('ÁGUA - PERDEU A VEZ')
                cont += 1
                time.sleep(2)
        else:
            print('-Jogador 2-')
            linha = input('Qual linha do seu ataque? ').upper()
            coluna = int(input('Qual coluna do seu ataque? '))
            linha = ord(linha) - 65

            if tabuP11[linha][coluna-1] == 'F' or tabuP11[linha][coluna-1] == 'A':
                print('JÁ JOGADO - PERDEU A VEZ')
                cont += 1
                time.sleep(2)
            elif tiro(tabuP1, linha, coluna):
                tabuP11[linha][coluna-1] = 'F'
                print('FOGO - SUA VEZ NOVAMENTE')
                pontuacaoP2 += 1
                time.sleep(2)
            else:
                tabuP11[linha][coluna-1] = 'A'
                print('ÁGUA - PERDEU A VEZ')
                cont += 1  
                time.sleep(2) 
        if pontuacaoP1 == quantNavios:
            print('JOGADOR 1 GANHOU!!')
            time.sleep(10)
            break
        elif pontuacaoP2 == quantNavios:
            print('JOGADOR 2 GANHOU!!')
            time.sleep(10)
            break

def tiro(tabu,linha,coluna):

        if tabu[linha][coluna-1] == 'N':
            return True
        else:
            return False