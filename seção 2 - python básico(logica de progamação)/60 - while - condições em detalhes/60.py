'''
usando while para definir o fim de uma compra em um mercado
'''

condicao = True
carrinho = []

while condicao:
    item = input('qual o próximo item da lista?: ')
    
    print(f'você possui os seguintes itens no carrinho: {carrinho}')
    
    finalizar_compra = input('Você deseja finalizar as compras?(S/N): ')
    if finalizar_compra == 'S':
        print('compra finalizada')
        print(f'o que você comprou: {carrinho}')
        break

    else:
        print('continuar compra')


