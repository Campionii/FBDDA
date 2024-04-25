# Faça um programa com uma função maior e menor, que leia uma lista com 5 valores informados pelo usuário
# e retorne esses valores e a posição deles

#Minha resolucao

"""""
lista = []

for ele in range(5):
    lista.append(int(input('Digite um valor: ')))

print(lista)
print(min(lista))
print(max(lista))

"""

# Resolução do professor

def maior(valores):
    maior_numero = valores[0]
    for ele in valores:
        if ele > maior_numero:
            maior_numero = ele
        return maior_numero

def menor(valores):
    menor_numero = valores[0]
    for ele in valores:
        if ele > menor_numero:
            menor_numero = ele
        return menor_numero

lista = []

for ele in range(5):
    lista.append(int(input('Digite um número: ')))

print(maior(lista))
print(menor(lista))
