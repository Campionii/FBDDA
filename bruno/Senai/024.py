# Escreva um programa que peça ao usuário uma senha e verifique se ela está correta (a senha correta é "python123").

senha = str(input('digite a senha: '))

if senha == 'python123':
    print('Seja Bem-Vindo!')

else:
    print('Senha incorreta')