import time

#Função que pergunta onde o usuário que atirar
def tiro():
    #Pergunta e valida a linha do ataque
    while True:
        lin = input('Qual linha do seu ataque? ').upper()
        if lin < 'A' or lin > 'J' or len(lin) > 1:
            print('ERRO')
            continue
        else:
            break
    #Pergunta e valida a coluna do ataque
    while True:
        colum = int(input('Qual coluna do seu ataque? '))
        if colum < 0 or colum > 10:
            print('ERRO')
            continue
        else:
            break
    
    """ 
    Tranforma a Letra da linha em número de acordo com a tabela ASCII e então diminui o valor de A(65), 
    assim, quando for digitado: A = 0; B = 1; C = 2... 
    """
    lin = ord(lin) - 65
    #Diminui 1 da coluna, Assim, quando for digitado: 1 = 0; 2 = 1; 3 = 2...
    colum -= 1

    return lin, colum

#Função que retorna o resultado do ataque
def resul_tiro(tabu, tabul, linha, coluna):
    #Testa se o local digitado já foi bombardeado, se sim, retorna False, passando a vez pro jogador
    if tabul[linha][coluna] == 'F' or tabul[linha][coluna] == 'A':
        print('JÁ BOMBARDEADO - PERDEU A VEZ')
        time.sleep(2)
        return False
    #Testa se o local digitado é um Navio, se sim, retorna True, e a vez continua sendo do mesmo jogador
    elif tabu[linha][coluna] == 'N':
        tabul[linha][coluna] = 'F'
        print('FOGO - SUA VEZ NOVAMENTE')
        time.sleep(2)
        return True
    #Testa se o local digitado é Água, se sim, retorna False, passando a vez pro jogador
    else:
        tabul[linha][coluna] = 'A'
        print('ÁGUA - PERDEU A VEZ')
        time.sleep(2)
        return False