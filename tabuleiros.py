from random import randint

#Função que cria os tabuleiros
def tabuleiro():
    tab = [['-']*10 for i in range(10)]

    return tab

#Função que distribui os navios no tabuleiro de frotas
def frotas(tabu, qtdNav):
    cont = 0
    tab = tabu

    #Impede que os navios encostem uns nos outros
    while cont < qtdNav:
        j = randint(0, 9)
        k = randint(0, 9)

        if j > 0 and k > 0 and tab[j-1][k-1] == 'N':
            continue
        if j > 0 and tab[j-1][k] == 'N':
            continue
        if j > 0 and k < 9 and tab[j-1][k+1] == 'N':
            continue
        if k > 0 and tab[j][k-1] == 'N':
            continue
        if tab[j][k] == 'N':
            continue
        if k < 9 and tab[j][k+1] == 'N':
            continue
        if j < 9 and k > 0 and tab[j+1][k-1] == 'N':
            continue
        if j < 9 and tab[j+1][k] == 'N':
            continue
        if j < 9 and k < 9 and tab[j+1][k+1] == 'N':
            continue
        tab[j][k] = 'N'
        cont += 1
    return tab