"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
""" ERROS POSSÍVEIS
IndexError: list assignment index out of range: a lista não tem esse índice
ValueError: invalid literal for int() with base 10: 'a': tentou converter um str para int
"""

lista_mercado = []

lista_mercado_enum = tuple(enumerate(lista_mercado))

while True:
    opcao_lista = input('Digite o que deseja fazer: [i]nserir [a]pagar [l]istar: ')

    if opcao_lista == 'i':
        adicionar_item = input('O que deseja adicionar na lista?: ')
        lista_mercado.append(adicionar_item)
    
    elif opcao_lista == 'a':
        apagar_item = input('Qual o índice que quer apagar?: ')
        try:
            apagar_item_int = int(apagar_item)
            del lista_mercado[apagar_item_int]
        except:
            print('Não tem esse índice na lista')
        """
        for indice, item_mercado in enumerate(lista_mercado): # parte antiga da função apagar índice 
            if indice == apagar_item:
                del lista_mercado[apagar_item]
        """
              
    elif opcao_lista == 'l':
        for indice, item_mercado in enumerate(lista_mercado):
            print(indice, item_mercado)
