'''
try: tentar executar o código
except: ocorreu um erro ao executar 

sempre tratar o input do usuário

if checa uma condição e segue o fluxo de acordo com essa condição
o try tenta executar o código. caso ache algum erro, pula direto para o except

'''
numero = input('digite um número: ')

try:
    numero_int = int(numero)
    print(f'o triplo de {numero_int} é {numero_int * 3 }')
except:
    print('isso não é um número')

'''


if numero.isdecimal():
    print(f'{numero} é um decimal')
else:
    print(f'{numero} não é um decimal')

if numero.isdigit():
    print(f'{numero} é um digito')
else:
    print(f'{numero} não é um dgito')

if numero.isnumeric():
    print(f'{numero} é numerico')
else:
    print(f'{numero} não é numerico')
'''