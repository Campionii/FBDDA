# Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
import time
print('BEM VINDO A SUA TABUADA ONLINE! \n')
n = int(input('Digite um numero para ver a tabuada: '))

for i in range(1, 11):
    time.sleep(0.7)
    print(f'{n} x {i} =', (n * i))

