from random import randint

#{{M. Pedro}}
#Função que cria os tabuleiros
def boards():
    brd = [['-']*10 for i in range(10)]

    return brd

#Função que distribui os navios no tabuleiro de frotas
def fleets(brd, countShips):
    cont = 0
    board = brd

    #Impede que os navios encostem uns nos outros
    while cont < countShips:
        l = randint(0, 9)
        c = randint(0, 9)

        if l > 0 and c > 0 and board[l-1][c-1] == 'N':
            continue
        if l > 0 and board[l-1][c] == 'N':
            continue
        if l > 0 and c < 9 and board[l-1][c+1] == 'N':
            continue
        if c > 0 and board[l][c-1] == 'N':
            continue
        if board[l][c] == 'N':
            continue
        if c < 9 and board[l][c+1] == 'N':
            continue
        if l < 9 and c > 0 and board[l+1][c-1] == 'N':
            continue
        if l < 9 and board[l+1][c] == 'N':
            continue
        if l < 9 and c < 9 and board[l+1][c+1] == 'N':
            continue
        board[l][c] = 'N'
        cont += 1
    return board