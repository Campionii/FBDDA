# Escreva um programa que leia uma frase, e mostre uma formatação adaptável de acordo com o tamanho da frase, coordenado por uma função
#
#
# Exemplo:
#        ----------------------------
#             Senai Show de bola
#        ----------------------------

def titulo(msg):
    print('---' * len(msg))
    print(msg.center(2 * len(msg)))
    print('---' * len(msg))

try:
    titulo('oi')
    titulo('Senai Show de Bola')

except TypeError:
    print('Informe apenas strings')
