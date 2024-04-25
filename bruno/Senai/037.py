# Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10
# e continue pedindo até que o usuário acerte o número.
# E no final, retorne também a quantidade de tentativas necessárias.

#jogada da maquina

from random import randint
pc = randint(1, 10)

#apresentacao

print('Jogo de adivinha?')


contador = 0
parada = 'S'
while parada != 'N':
    jogada = int(input('escolha um valor de 1 a 10: '))
    print(f'P1: {jogada}' f'\nPC: {pc}')

    if jogada == pc:
        print('Acertou')

    else:
        print('errou')

    parada = input('Deseja continuar [S/N] -> ').strip().upper()
    contador += 1










