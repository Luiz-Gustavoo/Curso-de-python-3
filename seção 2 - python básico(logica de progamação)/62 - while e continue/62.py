contador_idades = 0
contador_idades_int = int(contador_idades)

while contador_idades_int <=30:
    idade = input('qual a sua idade?: ')
    idade_int = int(idade)

    contador_idades_int =+1
    print(f'contador: {contador_idades_int}')

    if idade_int == 20:
        print('20 é inválido')
        continue
    
    print(f'idade: {idade_int}')


    if idade_int == 25:
        break


print('acabou') 
print('teste')



