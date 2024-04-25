# Crie um programa para jogar JOKEMPO, usando a função random.randint

# a = randint(1, 3)
# jogador-pedra = 3    #pc-pedra = 1
# jogador-papel = 2    #pc-papel = 2
# jogador-tesoura = 1  #pc-tesoura = 3

from random import randint

print('bem vindo ao Jokempô!')
print(' - pedra: 3 \n - papel: 2 \n - tesoura: 1')

jogador = int(input('Escolha uma jogada(DIGITE O NUMERO): '))

print(f'P1: {jogador}')

pc = randint(1, 3)

if pc == 1 and jogador == 1:
    print('P1: tesoura VS PC: Pedra... Vôce Perdeu!')

elif pc == 1 and jogador == 2:
    print('P1: Papel VS PC: Pedra... Vôce Ganhou!')

elif pc == 2 and jogador == 1:
    print('P1: Tesoura VS PC: Papel... Vôce Ganhou!')

elif pc == 2 and jogador == 3:
    print('P1: Pedra VS PC: Papel... Vôce Perdeu!')

elif pc == 3 and jogador == 2:
    print('P1: Papel VS PC: Tesoura... Vôce Perdeu!')

elif pc == 3 and jogador == 3:
    print('P1: Papel VS PC: Tesoura... Vôce Ganhou!')

elif pc == jogador:
    print('EMPATE!')

else:
    print('Coloque um dado valido (Numero 1 a 3!)')






