from tabuleiros import tabuleiro, tabuleiro2
from printjg import printTeste, printJogo
import os
import time


def novoJogo():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    while True:
        quantNavios = int(
            input('Digite a quantidade de navios de cada jogador [Máx = 10]: '))
        if quantNavios < 0 or quantNavios > 10:
            print('ERRO')
            time.sleep(1)
            continue
        else:
            break
    tabuP1 = tabuleiro(quantNavios)
    tabuP2 = tabuleiro(quantNavios)
    tabuP11 = tabuleiro2()
    tabuP22 = tabuleiro2()
    pontuacaoP1 = 0
    pontuacaoP2 = 0
    cont = 1
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    teste = input(
        'Deseja mostrar as frotas(Função de Teste)?[S ou N] ').upper()

    while True:
        if teste == 'S':
            printTeste(abc, tabuP1, tabuP2, tabuP11,
                       tabuP22, pontuacaoP1, pontuacaoP2)
        else:
            printJogo(abc, tabuP11, tabuP22, pontuacaoP1, pontuacaoP2)
        print()

        if pontuacaoP1 == quantNavios:
            print('JOGADOR 1 GANHOU!!')
            time.sleep(10)
            break
        elif pontuacaoP2 == quantNavios:
            print('JOGADOR 2 GANHOU!!')
            time.sleep(10)
            break

        if cont % 2 != 0:
            print('-Jogador 1-')
            while True:
                linha = input('Qual linha do seu ataque? ').upper()
                if linha < 'A' or linha > 'J' or len(linha) > 1:
                    print('ERRO')
                    continue
                else:
                    break
            while True:
                coluna = int(input('Qual coluna do seu ataque? '))
                if coluna < 0 or coluna > 10:
                    print('ERRO')
                    continue
                else:
                    break
            linha = ord(linha) - 65
            coluna -= 1

            if tabuP22[linha][coluna] == 'F' or tabuP22[linha][coluna] == 'A':
                print('JÁ BOMBARDEADO - PERDEU A VEZ')
                cont += 1
                time.sleep(2)
            elif tiro(tabuP2, linha, coluna):
                tabuP22[linha][coluna] = 'F'
                print('FOGO - SUA VEZ NOVAMENTE')
                pontuacaoP1 += 1
                time.sleep(2)
            else:
                tabuP22[linha][coluna] = 'A'
                print('ÁGUA - PERDEU A VEZ')
                cont += 1
                time.sleep(2)
        else:
            print('-Jogador 2-')
            while True:
                linha = input('Qual linha do seu ataque? ').upper()
                if linha < 'A' or linha > 'J' or len(linha) > 1:
                    print('ERRO')
                    continue
                else:
                    break
            while True:
                coluna = int(input('Qual coluna do seu ataque? '))
                if coluna < 0 or coluna > 10:
                    print('ERRO')
                    continue
                else:
                    break
            linha = ord(linha) - 65
            coluna -= 1

            if tabuP11[linha][coluna] == 'F' or tabuP11[linha][coluna-1] == 'A':
                print('JÁ JOGADO - PERDEU A VEZ')
                cont += 1
                time.sleep(2)
            elif tiro(tabuP1, linha, coluna):
                tabuP11[linha][coluna] = 'F'
                print('FOGO - SUA VEZ NOVAMENTE')
                pontuacaoP2 += 1
                time.sleep(2)
            else:
                tabuP11[linha][coluna] = 'A'
                print('ÁGUA - PERDEU A VEZ')
                cont += 1
                time.sleep(2)


def tiro(tabu, linha, coluna):

    if tabu[linha][coluna] == 'N':
        return True
    else:
        return False


def resul_tiro():
    if tabuP11[linha][coluna] == 'F' or tabuP11[linha][coluna-1] == 'A':
        print('JÁ JOGADO - PERDEU A VEZ')
        cont += 1
        time.sleep(2)
    elif tiro(tabuP1, linha, coluna):
        tabuP11[linha][coluna] = 'F'
        print('FOGO - SUA VEZ NOVAMENTE')
        pontuacaoP2 += 1
        time.sleep(2)
    else:
        tabuP11[linha][coluna] = 'A'
        print('ÁGUA - PERDEU A VEZ')
        cont += 1
        time.sleep(2)
