# Escreva um programa que verifique se uma frase é um palíndromo.

#resolução do professor
palavra = input('Digite algo: ').lower().strip()
compatibilidade = 0

for i in range(0, len(palavra)):
    if palavra[i] == palavra[-i-1]:
        compatibilidade += 1

if compatibilidade == len(palavra):
    print('é palindromo')
else:
    print('Não é')


#minha resolução
p = 'ararA'
print(p[::-1])

