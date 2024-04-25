#Escreva um programa que leia 10 número, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma
soma = 0
for i in range(1, 11):
    num = float(input('Um número: '))
    if num % 2 == 0:
        soma = soma + num


print(f'A soma é {soma}')






