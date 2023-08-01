"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_mercado = []

lista_mercado_enum = tuple(enumerate(lista_mercado))

while True:
    opcao_lista = input('Digite o que deseja fazer: [i]nserir [a]pagar [l]istar: ')

    if opcao_lista == 'i':
        adicionar_item = input('O que deseja adicionar na lista?: ')
        lista_mercado.append(adicionar_item)
    
    elif opcao_lista == 'a':
        apagar_item = int(input('Qual o índice que quer apagar?: '))
        for indice, item_mercado in enumerate(lista_mercado):
            if indice == apagar_item:
                lista_mercado.pop(apagar_item)
            
    elif opcao_lista == 'l':
        for indice, item_mercado in enumerate(lista_mercado):
            print(indice, item_mercado)