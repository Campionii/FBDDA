#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input(f'Qual numero deseja saber seu dobro,triplo e raiz: '))

d = n * 2
t = n * 3
r = n ** 1/2

print(f' Numero: {n} \n dobro: {d:.2f} \n triplo: {t:.2f} \n raiz: {r:.2f}')
