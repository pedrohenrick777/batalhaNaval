import time

#{{Olivia}}
#Função que pergunta onde o usuário que atirar
def shot():
    #Pergunta e valida a linha do ataque
    while True:
        line = input('Qual linha do seu ataque? ').upper()
        if line < 'A' or line > 'J' or len(line) > 1:
            print('ERRO')
            continue
        else:
            break
    #Pergunta e valida a coluna do ataque
    while True:
        column = int(input('Qual coluna do seu ataque? '))
        if column < 0 or column > 10:
            print('ERRO')
            continue
        else:
            break
    
    """ 
    Tranforma a Letra da linha em número de acordo com a tabela ASCII e então diminui o valor de A(65), assim, quando for digitado: A = 0; B = 1; C = 2... 
    """
    line = ord(line) - 65
    #Diminui 1 da coluna, Assim, quando for digitado: 1 = 0; 2 = 1; 3 = 2...
    column -= 1

    return line, column

#Função que retorna o resultado do ataque
def result_shot(boardTP, boardP, line, column):
    #Testa se o local digitado já foi bombardeado, se sim, retorna False, passando a vez pro jogador
    if boardP[line][column] == 'F' or boardP[line][column] == 'A':
        print('JÁ BOMBARDEADO - PERDEU A VEZ')
        time.sleep(2)
        return False
    #Testa se o local digitado é um Navio, se sim, retorna True, e a vez continua sendo do mesmo jogador
    elif boardTP[line][column] == 'N':
        boardP[line][column] = 'F'
        print('FOGO - SUA VEZ NOVAMENTE')
        time.sleep(2)
        return True
    #Testa se o local digitado é Água, se sim, retorna False, passando a vez pro jogador
    else:
        boardP[line][column] = 'A'
        print('ÁGUA - PERDEU A VEZ')
        time.sleep(2)
        return False