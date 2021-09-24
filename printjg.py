import os


def printTeste(abcd, t1, t2, t11, t22, pontuacaoP1, pontuacaoP2):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print(''' 
            Jogador 1                              Frota Jogador 1
   |1  2  3  4  5  6  7  8  9  10           |1  2  3  4  5  6  7  8  9  10
---------------------------------        ---------------------------------''')
    for i in range(10):
        print(f'{abcd[i]}  |', end='')
        for j in range(10):
            print(f'{t11[i][j]:3}', end='')
        print(end='       ')

        print(f'{abcd[i]}  |', end='')
        for k in range(10):
            print(f'{t1[i][k]:3}', end='')
        print()
    print()
    print(f'Pontuação P1 = {pontuacaoP1}')

    print()
    print(''' 
            Jogador 2                              Frota Jogador 2
   |1  2  3  4  5  6  7  8  9  10           |1  2  3  4  5  6  7  8  9  10
---------------------------------        ---------------------------------''')
    for i in range(10):
        print(f'{abcd[i]}  |', end='')
        for j in range(10):
            print(f'{t22[i][j]:3}', end='')
        print(end='       ')

        print(f'{abcd[i]}  |', end='')
        for k in range(10):
            print(f'{t2[i][k]:3}', end='')
        print()
    print()
    print(f'Pontuação P2 = {pontuacaoP2}')


def printJogo(abcd, t11, t22, pontuacaoP1, pontuacaoP2):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print(''' 
            Jogador 1                                 Jogador 2
   |1  2  3  4  5  6  7  8  9  10           |1  2  3  4  5  6  7  8  9  10
---------------------------------        ---------------------------------''')
    for i in range(10):
        print(f'{abcd[i]}  |', end='')
        for j in range(10):
            print(f'{t11[i][j]:3}', end='')
        print(end='       ')

        print(f'{abcd[i]}  |', end='')
        for k in range(10):
            print(f'{t22[i][k]:3}', end='')
        print()
    print()
    print(f'''
    Pontuação P1 = {pontuacaoP1}
    Pontuação P2 = {pontuacaoP2}''')
