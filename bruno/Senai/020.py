# Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

# Ter idade entre 16 e 69 anos, sendo que os candidatos a doadores com menos de 18 anos deverão estar acompanhados pelos pais ou por responsável legal;
# Pesar no mínimo 50 Kg com desconto de vestimentas;
# O limite de idade para a primeira doação é de 60 anos;
# Não estar em jejum;
# Ter dormido pelo menos 6 horas antes da doação;
# Não ter ingerido bebidas alcoólicas nas 12 horas anteriores à doação;
# Não fumar pelo menos duas horas antes da doação 

import sys

while True:
    idade = int(input('Qual a sua idade? '))
    
    if idade > 69:
        print('Esta idade é muito avançada para doação de sangue.')
        sys.exit()

    elif idade < 16:
        print('A doação de sangue é permitida a partir de 16 anos.')
        sys.exit()

    else:
        print('Ok')
        break

peso = float(input('Qual o seu peso? '))

if peso < 50:
    print('Você não tem o peso mínimo (50kg).')
    sys.exit()
else:
    print('Ok')

jejum = str(input('Está em jejum? (sim/não) '))

if jejum.lower() == 'sim':
    print('Você não deve estar em jejum para a doação.')
    sys.exit()
elif jejum.lower() == 'não' or jejum.lower() =='nao' or jejum.lower() =='n':
    print('Ok')
else:
    print('Resposta inválida')
    sys.exit()

sono = int(input('Dormiu quantas horas esta noite? '))

if sono > 5:
    print('Ok')
else:
    print('Você não dormiu o suficiente.')
    sys.exit()

bebida = str(input('Ingeriu bebidas alcoólicas (nas últimas 12h)? (sim/não) '))

if bebida.lower() == 'sim':
    print('Não é permitido a doação com a ingestão de bebidas 12h antes.')
    sys.exit()
elif bebida.lower() == 'não' or bebida.lower() =='nao' or bebida.lower() =='n':

    print('Ok')
else:
    print('Resposta inválida')
    sys.exit()

fumar = str(input('Fumou nas últimas 2h? (sim/não) '))

if fumar.lower() == 'nao' or fumar.lower() == 'n' or fumar.lower() == 'não':
    print('Você está nos critérios para um exame de sangue :) ')
else:
    print('Você não pode fumar nas últimas 2h.')
    sys.exit()
