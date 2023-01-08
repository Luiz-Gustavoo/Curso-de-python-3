'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

entrada_hora = input('digite a hora atual: ')

if entrada_hora.isdigit():
    entrada_hora_int = int(entrada_hora)

    if (entrada_hora_int >= 0) and (entrada_hora_int <= 11):
        print('bom dia')

    elif(entrada_hora_int >= 12) and (entrada_hora_int <= 17):
        print('boa tarde')

    elif(entrada_hora_int >= 18) and (entrada_hora_int <= 23):
        print('boa noite')
else:
    print('você não digitou um número')