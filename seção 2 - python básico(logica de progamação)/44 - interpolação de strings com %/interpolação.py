"""
interpolação de strings é basicamente a mesma coisa que formatação de strings com format

 s - string
 i e d - int
 f - float
 x e X - hexadecimal
 """

 # formatação com format
nome = 'luiz'
preco = 99.90
format = '{}, o preço é de R${:.2f}'.format(nome, preco)
print(format)

# interpolação

interpolacao = '%s, o preço é de R$%.2f' % (nome, preco)
print(interpolacao)

