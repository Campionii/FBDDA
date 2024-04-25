# Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos







#tenho q arrumaaaaaaaaaaaaaar





maior = None
menor = None

for ele in range(0, 7):
    peso = float(input('digite seu peso: '))

    '''
    #1
    if maior == None and menor == None
    maior = peso
    menor = peso
    
    '''

    #2
    if ele == 0:
        maior = menor
        menor = maior

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print(f'O maior é {maior}'
      f'\nO menor é {menor}')