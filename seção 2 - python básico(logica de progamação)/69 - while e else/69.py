string = 'garrafa'
contador = 0
letra_f = ''
while contador <len(string):
    
    letra_atual = string[contador]

    if letra_atual == 'f':
        letra_f = letra_atual
        print('letra f')

    print(letra_atual)
    contador+=1
    
else:
    print('A letra {} foi encontrada'.format(letra_f))        

print('fora do while')