'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
numero = input('digite um número inteiro: ')


if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'"{numero_int}" é par')
    else:
        print(f'"{numero_int}" não é par')    

else:
    print(f'"{numero}" não é inteiro')    


 
