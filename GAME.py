#jogador_nome = 'Guilherme'
#jogador_ataque = 10
#jogador_cura = 16
#saúde = 100

#player = ['Guilherme', 10, 16, 100]

from random import randint

game_runnig = True
resultados_jogo = []

def calculate_monstro_ataque():
    return randint(monstro['ataque_min'], monstro['ataque_max'])

def game_ends(nome_vencedor):
    print(f'{nome_vencedor} venceu o jogo')

while game_runnig == True:
    counter = 0
    novo_jogo = True
    jogador = {'nome': 'Guilherme', 'ataque': 15, 'cura': 20, 'saúde': 100}
    monstro = {'nome': 'Matozila', 'ataque_min': 12, 'ataque_max': 20, 'saúde': 100}

    print('___' * 7)
    print('Escolha o nome do jogador')
    jogador['nome'] = input()

    print('___' * 7)
    print(jogador['nome'] + ' tem ' + str(jogador['saúde']) + ' de saúde ')
    print(monstro['nome'] + ' tem ' + str(monstro['saúde']) + ' de saúde ')

    while novo_jogo == True:

        counter = counter + 1
        jogador_won = False
        monstro_won = False

        print('___' * 7)
        print('Selecione uma ação')
        print('1) Ataque')
        print('2) Cura')
        print('3) Sair')
        print('4) Mostrar resultados')

        jogador_choice = input()

        if jogador_choice == '1':
            monstro['saúde'] = monstro['saúde'] - jogador['ataque']
            if monstro['saúde'] <= 0:
                jogador_won = True

            else:
                jogador['saúde'] = jogador['saúde'] - calculate_monstro_ataque()
                if jogador['saúde'] <= 0:
                    monstro_won = True

        elif jogador_choice == '2':
            jogador['saúde'] = jogador['saúde'] + jogador['cura']
            monstro_ataque = randint(monstro['ataque_min'], monstro['ataque_max'])
            jogador['saúde'] = jogador['saúde'] - monstro_ataque
            if jogador['saúde'] <= 0:
                monstro_won = True

        elif jogador_choice == '3':
            novo_jogo = False
            game_runnig = False

        elif jogador_choice == '4':
            for item in resultados_jogo:
                print(item)

        else:
            print('escolha invalida')

        if jogador_won == False and monstro_won == False:
            print(jogador['nome'] + ' tem ' + str(jogador['saúde']) + ' de saúde sobrando ')
            print(monstro['nome'] + ' tem ' + str(monstro['saúde']) + ' de saúde sobrando ')

        elif jogador_won:
            game_ends(jogador['nome'])
            resultado_rodada = {'nome': jogador['nome'], 'saúde': jogador['saúde'], 'rodada': counter}
            resultados_jogo.append(resultado_rodada)
            print(resultados_jogo)
            novo_jogo = False

        elif monstro_won:
            game_ends(monstro['nome'])
            resultado_rodada = {'nome': monstro['nome'], 'saúde': monstro['saúde'], 'rodada': counter}
            resultados_jogo.append(resultado_rodada)
            print(resultados_jogo)
            novo_jogo = False

