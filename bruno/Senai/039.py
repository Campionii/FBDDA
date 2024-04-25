# Faça um programa que leia um número e retorne o fatorial !
#
# 4! = 4 x 3 x 2 x 1

numero = int(input('Um numero para ser fatoriado: '))

contador = 1
fat = 1
while numero > contador:
    contador += 1
    fat = contador - fat

print(f'O fatorial é {fat}')



