import  sys
#Variaveis Globais#

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
jogadores = -1
flag = 1
def verifica_potuacao(arena,jog):
    for i in range(3):
        soma = 0        for j in range(3):
            soma = soma  + arena[i][j]
        if (soma == 3):
            print("Jogador 1 ganhou")
            sys.exit()
        if (soma == -3):
            print("Jogador 2 ganhou")
            sys.exit()
    for j in range(3):
        soma = 0        for i in range(3):
            soma = soma + arena[i][j]
        if (soma == 3):
            print("Jogador 1 ganhou")
            sys.exit()
        if (soma == -3):
            print("Jogador 2 ganhou")
            sys.exit()

    if (arena[0][0]+arena[1][1]+arena[2][2]) == 3:
            print("Jogador 1 ganhou")
            sys.exit()
    if (arena[0][0]+arena[1][1]+arena[2][2]) == -3:
            print("Jogador 2 ganhou")
            sys.exit()
    if (arena[2][0]+arena[1][1]+arena[0][2]) == 3:
            print("Jogador 1 ganhou")
            sys.exit()
    if (arena[2][0]+arena[1][1]+arena[0][2]) == -3:
            print("Jogador 2 ganhou")
            sys.exit()
def jogada(arena,jog,flag):
    for i in range(3):
        for j in range(3):
            if (arena[i][j]) ==0:
                verifica_potuacao(arena, jog)
                jogador(arena, jog, flag)
    verifica_potuacao(arena, jog)
    print("Jogo empatou")
    sys.exit()

def jogador(arena,jog,flag):
    if (flag == 1):
        if jog == -1:
            jog = 1            print("Primeiro Jogador a jogar")
            print(matriz[0])
            print(matriz[1])
            print(matriz[2])
        else:
            jog = -1            print("Segundo Jogador a jogar")
            print(matriz[0])
            print(matriz[1])
            print(matriz[2])
    num = input("Escolha uma zona")
    if (num == '1'):
        if (arena[2][0] == 0):
            arena[2][0] = jog
        else:
            print("Selecione outra zona")
            flag = 0            jogador(arena,jog,flag)

    if num == '2':
        if (arena[2][1] == 0):
            arena[2][1] = jog
        else:
            print("Selecione outra zona")
            flag = 0            jogador(arena, jog,flag)

    if num == '3':
        if (arena[2][2] == 0):
            arena[2][2] = jog
        else:
            print("Selecione outra zona")
            flag = 0            jogador(arena, jog,flag)
    if num == '4':
        if (arena[1][0] == 0):
            arena[1][0] = jog

        else:
            print("Selecione outra zona")
            flag = 0            jogador(arena, jog,flag)

    if num == '5':
        if (arena[1][1] == 0):
            arena[1][1] = jog

        else:
            print("Selecione outra zona")
            flag = 0            jogador(arena, jog,flag)
    if num == '6':
        if (arena[1][2] == 0):
            arena[1][2] = jog

        else:
            print("Selecione outra zona")
            flag = 0            jogador(arena, jog,flag)

    if num == '7':
        if (arena[0][0] == 0):
            arena[0][0] = jog

        else:
            print("Selecione outra zona")
            flag = 0            jogador(arena, jog,flag)
    if num == '8':
        if (arena[0][1] == 0):
            arena[0][1] = jog

        else:
            print("Selecione outra zona")
            flag = 0            jogador(arena, jog, flag)
    if num == '9':
        if (arena[0][2] == 0):
            arena[0][2] = jog

    if (num != '1' and num != '2' and num != '3' and
 num != '4'and num != '5'and num != '6'and num != '7' and
 num != '8'and num != '9') :
        print("Valo indisponivel")
        if num == '':
            print("Por favor digite um valor e tente novamente")
            
        flag = 1        if jog == -1:
            jog = 1        else:
            jog = -1        jogador(arena, jog, flag)

    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    flag = 1    jogada(arena,jog,flag)
#Gatilho para iniciar o jogo
jogada(matriz,jogadores,flag)
