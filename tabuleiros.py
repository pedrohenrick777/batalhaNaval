from random import randint

def tabuleiro(qtdNav):
    tab = [['-']*10 for i in range(10)]
    cont = 0

    while cont < qtdNav:
        j = randint(0, 9)
        k = randint(0, 9)

        if j>0 and k>0 and tab[j-1][k-1] == 'N':
            continue
        if j>0 and tab[j-1][k] == 'N':
            continue
        if j>0 and k<9 and tab[j-1][k+1] == 'N':
            continue
        if k>0 and tab[j][k-1] == 'N':
            continue
        if tab[j][k] == 'N':
            continue
        if k<9 and tab[j][k+1] == 'N':
            continue
        if j<9 and k>0 and tab[j+1][k-1] == 'N':
            continue
        if j<9 and tab[j+1][k] == 'N':
            continue
        if j<9 and k<9 and tab[j+1][k+1] == 'N':
            continue
        tab[j][k] = 'N'
        cont += 1
    return tab

def tabuleiro2():
    tab = [['-']*10 for i in range(10)]

    return tab


    

