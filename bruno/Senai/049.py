# Crie um programa que tenha a função área(),
# que receba as dimensões de um muro retangular e mostra a área do terreno

def area(a, b):
    resultado = a * b
    print(f'A area do terreno é {resultado}')


def area_terreno(a,b):
    resultado = a * b
    return resultado


print(area_terreno(2,3))
area(4,5)
