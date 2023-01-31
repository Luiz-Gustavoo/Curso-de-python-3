"""
while(repetição): executa uma ação enquanto uma ação for verdadeira
"""

condicao = True
contador_nome = 0
contador_nome_int = int(contador_nome)

while condicao:
    nome = input('qual é o seu nome: ')
    print(f'seu nome é {nome}')

    contador_nome_int = contador_nome_int + 1
    print(f'ciclo do while: {contador_nome_int}')
    
    if contador_nome_int == 3:
        break        

print('acabou os ciclos do while')