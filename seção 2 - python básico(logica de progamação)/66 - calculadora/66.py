"""
calculadora com while
não esta perfeita. pode haver crash
"""

calculadora_ativa = True

while calculadora_ativa == True:

    numero1 = input('digite um número: ')
    numero1_int = int(numero1)
    
    numero2 = input('digite um número: ')
    numero2_int = int(numero2)

    lista_operadores = ['+', '-', '/', '*']
    operador = input('escolha um operador (+, -, /, *): ')
    

    while operador not in lista_operadores:
        print('operador inválido')
        operador = input('escolha um operador (+, -, /, *): ')
        if operador in lista_operadores:
            break
        else:
            continue

       
    if operador == '+':
        resultado = numero1_int + numero2_int
        print(resultado)
    elif operador == '-':
        resultado = numero1_int - numero2_int
        print(resultado)   

    elif operador == '/':
        resultado = numero1_int / numero2_int     
        print(resultado)

    elif operador == '*':
        resultado = numero1_int * numero2_int
        print(resultado)    
    else:
        print('voltar')


sair = input('deseja sair? [s][n]')
if sair == 's':
    calculadora_ativa = False
    print('calculadora desativada')
        
if sair == 'n':
    print('calculadora ativa')
   