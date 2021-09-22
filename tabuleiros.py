from random import randint

def tabuleiro(qtdNav):
    tab = [['-']*10 for i in range(10)]
    cont = 0

    while cont < qtdNav:
        j = randint(0, 9)
        k = randint(0, 9)

        if j == 0:
            if k == 0:
                if tab[j][k] == '-' and tab[j][k+1] == '-' and tab[j+1][k] == '-' and tab[j+1][k+1] == '-':
                    tab[j][k] = 'N'
                    cont += 1
            elif k == 9:
                if tab[j][k] == '-' and tab[j][k-1] == '-' and tab[j+1][k] == '-' and tab[j+1][k-1] == '-':
                    tab[j][k] = 'N'
                    cont += 1
            else:
                if tab[j][k] == '-' and tab[j][k-1] == '-' and tab[j+1][k] == '-' and tab[j+1][k-1] == '-' and  tab[j][k+1] == '-' and tab[j+1][k+1] == '-':
                    tab[j][k] = 'N'
                    cont += 1
        elif k == 0:
            if j == 9:
                if tab[j][k] == '-' and tab[j-1][k] == '-' and tab[j][k+1] == '-' and tab[j-1][k+1] == '-':
                    tab[j][k] = 'N'
                    cont += 1
            else:
                if tab[j][k] == '-' and tab[j-1][k] == '-' and tab[j][k+1] == '-' and tab[j-1][k+1] == '-' and tab[j+1][k] == '-' and tab[j+1][k+1] == '-':
                    tab[j][k] = 'N'
                    cont += 1                    
        elif j == 9:
            if k == 9:
                if tab[j][k] == '-' and tab[j-1][k] == '-' and tab[j-1][k-1] == '-' and tab[j][k-1] == '-':
                    tab[j][k] = 'N'
                    cont += 1
            else:
                if tab[j][k] == '-' and tab[j-1][k] == '-' and tab[j][k+1] == '-' and tab[j][k-1] == '-' and tab[j-1][k+1] == '-' and tab[j-1][k-1] == '-':
                    tab[j][k] = 'N'
                    cont += 1
        elif k == 9:
            if tab[j][k] == '-' and tab[j][k-1] == '-' and tab[j-1][k] == '-' and tab[j+1][k] == '-' and tab[j+1][k-1] == '-' and tab[j-1][k-1] == '-':
                tab[j][k] = 'N'
                cont += 1
        else:
            if tab[j][k] == '-' and tab[j][k-1] == '-' and tab[j-1][k] == '-' and tab[j+1][k] == '-' and tab[j+1][k-1] == '-' and tab[j-1][k-1] == '-' and tab[j-1][k+1] == '-' and tab[j][k+1] == '-' and tab[j+1][k+1] == '-':
                tab[j][k] = 'N'
                cont += 1
    
    return tab

def tabuleiro2():
    tab = [['-']*10 for i in range(10)]

    return tab


    

