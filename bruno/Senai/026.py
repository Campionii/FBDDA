# Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a
# faixa ideal,
# acima ou
# abaixo do IMC ideal.


#Abaixo de 18,5: Abaixo do peso
#18,5 a 24,9: Peso normal
#25 a 29,9: Sobrepeso
#30 ou mais: Obesidade

peso = float(input('Qual o seu peso(Kg): '))

altura = float(input('Qual a sua altura(m): '))

imc = peso / (altura ** 2)

if imc >= 30: 
    print(f'IMC: {imc:.2f} "Obesidade"')

elif imc >= 25: 
    print(f'IMC: {imc:.2f} "Sobrepeso"')

elif imc >= 18.5: 
    print(f'IMC: {imc:.2f} "Peso normal"')

else:
    print(f'IMC: {imc:.2f} "Abaixo do peso"')

