"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('digite o seu nome: ')
idade = input('digite a sua idade: ')
nome_str = str(nome)
idade_int = int(idade)

if nome_str and idade_int:
    print('seu nome é %s' %(nome_str))
    print('seu nome invertido é {}'.format(nome_str[::-1]))
    if  ' ' in nome_str:
        print('seu nome possui espaços')
    else:
        print('seu nome não possui espaços')    
    print(f'seu nome possui {len(nome_str)} letras')    
    print(f'a primeira letra do seu nome é: {nome_str[0]}')
    print(f'a última letra do seu nome é: {nome_str[-1:]}')
else:
    print('você deixou campos vazios')



