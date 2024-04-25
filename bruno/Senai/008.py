#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.

s = float(input(f'Qual o seu sálario? '))
reajuste_s = s * 60/100
novo_s = s + reajuste_s

print(f'O salario de {s} com o reajuste de 60% ficou: {novo_s}')