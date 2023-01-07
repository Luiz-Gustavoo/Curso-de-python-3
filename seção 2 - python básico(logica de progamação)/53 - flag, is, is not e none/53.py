'''
 saber se o interpretador passou por um local

passou_no_if = None
input = input('digite sua senha: ')

if input:
    print(input)
else:
    print('input vazio')
'''
pedir_senha = input('digite sua senha: ')
digitou_senha = None

if pedir_senha:
    print('usuário digitou no campo senha')
    digitou_senha = True    
else:
    print('usuário não digitou no campo senha') 

if digitou_senha is not None:
    print('passou no if')

if digitou_senha is None:
    print('não passou no if')  

