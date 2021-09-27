import os

#Função que exibe o tabuleiro de frotas(TESTE)
def printTeste(t1, t2):

    print()
    print_mapa(t1, t2)#Printa o tabuleiro de frota do Jogador 1 e Jogador 2

#Função que exibe os tabuleiros de jogo
def printJogo(t11, t22, pontuacaoP1, pontuacaoP2):
    limpar_tela()

    print_mapa(t11, t22)#Printa o tabuleiro do Jogador 1 e Jogador 2
    print()
    #Exibe a pontuação dos jogadores
    print(f'''
    Pontuação P1 = {pontuacaoP1}
    Pontuação P2 = {pontuacaoP2}''')

#Função que printa os tabuleiros
def print_mapa(tab, tabu):
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
            print(f'{tab[i][j]:3}', end='')
        print(end='       ')

        print(f'{abcd[i]}  |', end='')
        for k in range(10):
            print(f'{tabu[i][k]:3}', end='')
        print()



#Função para limpar a tela
def limpar_tela():
    """ 
    Testa se o sistema é windows(nt), se sim, executa o comando cls(Limpa o CMD), se não, executa 
    o respectivo comando para Unix (clear)
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
