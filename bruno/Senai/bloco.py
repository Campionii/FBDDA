"""

# Calculadora
print(5 + 10)
print(1 + 1)
print(1 - 10)

# String / Texto
print('Meu nome é Bruno')

# Entrada de Dados
N1 = int(input('Digite a sua idade: '))
Idade_Nova = N1 + 1000000
print(f'A sua idade é {Idade_Nova}')

# Laço de repetição
# Inicializando a variável para armazenar a soma das notas
soma_nota = 0

# Lendo as 6 notas do usuário
for i in range(6):
    nota = float(input(f'Qual sua nota {i + 1}: '))
    soma_nota += nota

# Calculando a média
media = soma_nota / 6

# Exibindo a média final
print(f'A sua média: {media:.2f}')  # Utilizando :.2f para formatar a média com duas casas decimais



#STRINGS

# Fatiamento


Senai = ‘Luis Eulalio’

Senai[3]  # s
Senai[3:9]  # s Eula
Senai[3:10:2]  # sEll
Senai[:5]  # Luis
Senai[7:]  # lalio
Senai[3::2]  # sEllo



# Análise

Senai = ‘Luis
Eulalio’
len(Senai)  # Retorna o Tamanho da string  (12)
Senai.count(‘l’)  # Retorna a contagem de (‘l’)  (2)
Senai.count(‘Lu’)  # Retorna a contagem de (‘Lu’) (1)

‘Lu’ in Senai  # Retorna se existe ‘Lu’, em Senai
TRUE / FALSE
Senai.find(‘Lu’)  # Retorna a posição de procura


# Transformação


Senai = ‘Luis Eulalio’

Senai.replace(‘L’, ‘P’)  # substitui L por P
Senai.upper()  # todas as letras serão maíscula
Senai.lower()  # todas as letras serão minúsculas
Senai.capitalize()  # apenas a primeira letra da primeira palavra estará em maiúsculo

Senai.title()  # todas as primeiras letras das palavras estarão em maiúsculo
Senai.split()  # separa a sting em um lista em
Senai.rstrip()  # remove espaços á direita
Senai.lstrip()  # remove espaços á esquerda


#Atividade extra de MRUV

# Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário
# s =S0 + V^T

posicao_inicial = float(input('Informe a posição inicial (em metros): '))
v = float(input('Informe a velocidade (em metros por segundo): '))
t = float(input('Informe o tempo (em segundos): '))
a = float(input('iforme a aceleração (em metros por segundo ao quadrado):  '))

MRUV = posicao_inicial + (v * t) + (((a * t)**2) / 2)

print(f'A posição do objeto no tempo {t} é de {MRUV}m')


#Estruturas de Repetição

#Loop For


for contador in range(1, 10):
    print('*')

for contador in range(1, 10):
    print(contador, end=' ')

soma = 0
for i in range(1, 11):
    idade = int(input('Digite a sua idade: '))
    soma = soma + idade


#While

#numerico

# contador = 0
# while contador < 5:
#     print('Oi')
#     contador += 1

#string

contador = 0
resposta = 'S'
while resposta != 'N':
    print('01')
    resposta = input('Deseja continuar [S/N] -> ').strip().upper()
    contador += 1

#try and except

while True:
    try:
        numero = int(input('Digite um número: '))

    except ZeroDivisionError:
        print('Erro ao dividir por 0')

    except ValueError:
        print('Digite apenas números')

    except:
        print('ERRO')


def area(a,b):
    A = a * b

    return A

def titulobonito(msg):
    print('-------------------')
    print(msg)
    print('-------------------')


def fatorial(n):
    fat = 1
    numero = 1
    while n + 1 > numero:
        fat = numero * fat
        numero += 1
    return fat



titulobonito('oi')
resultado = fatorial(5)
print(f'{fatorial(5)}')



#TUPLAS

carro = ('Ferrari', 'Vermelha', '2023')
print(carro)

for ele in carro:
    print(ele)

for ele in range(0, len(carro)):
    print(carro[ele])


a = (1,2,3,4)
b = (5,6,7,8)
c = a + b
print(c)
print(sorted(c))
print(sum(c))
print(max(c))
print(min(c))

"""''

# LISTA

carro = ['Ferrari', 'Vermelha', '2024']
print(carro)
print(carro[0])
carro[1] = 'Amarelo'
carro.append('OI')
print(carro)
carro.pop(0)
print(carro)
carro.remove('OI')
print(carro)


idades = [1,2,3,4,5,6,7]
print(max(idades))
print(min(idades))
print(len(idades))
print(sorted(idades))
print(sum(idades)/len(idades))

for ele in range(3):
    idades.append(int(input('Digite uma idade: ')))
