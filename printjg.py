import os

#{{Pedro P.}}
#Função que exibe o tabuleiro de frotas(TESTE)
def print_test(tabTP1, tabTP2):

    print()
    print_map(tabTP1, tabTP2)#Printa o tabuleiro de frota do Jogador 1 e Jogador 2

#Função que exibe os tabuleiros de jogo
def print_game(tabP1, tabP2, scoreP1, scoreP2):
    clean_screen()

    print_map(tabP1, tabP2)#Printa o tabuleiro do Jogador 1 e Jogador 2
    print()
    #Exibe a pontuação dos jogadores
    print(f'''
    Pontuação Jogador 1 = {scoreP1}
    Pontuação Jogador 2 = {scoreP2}''')

#Função que printa os tabuleiros
def print_map(tab1, tab2):
    #Vetor usado para indicar qual é a linha do tabuleiro
    abcd = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    #Printa os escopos dos tabuleiros
    print(''' 
            Jogador 1                                 Jogador 2
   |1  2  3  4  5  6  7  8  9  10           |1  2  3  4  5  6  7  8  9  10
---------------------------------        ---------------------------------''')

    for i in range(10):
        print(f'{abcd[i]}  |', end='')
        for j in range(10):
            print(f'{tab1[i][j]:3}', end='')
        print(end='       ')

        print(f'{abcd[i]}  |', end='')
        for k in range(10):
            print(f'{tab2[i][k]:3}', end='')
        print()



#Função para limpar a tela
def clean_screen():
    """ 
    Testa se o sistema é windows(nt), se sim, executa o comando cls(Limpa o CMD), se não, executa 
    o respectivo comando para Unix (clear)
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
