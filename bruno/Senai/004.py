#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
#V = (4/3) . π . r³
#A = 4 . π . r²

r = float(input('Qual o raio? '))
v = 4/3 * 3.1415 * r**3
a = 4 * 3.1415 * r**2

print(f'volume da Esfera:{v:.2f} Área da Esfera: {a:.2f}!')
