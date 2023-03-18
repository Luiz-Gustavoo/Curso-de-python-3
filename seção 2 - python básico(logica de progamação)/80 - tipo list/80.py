# list() connverter algo em lista
# lista é mutavel: pode mudar os valores 
# é melhor deletar indices e valores no final da lista
    # em strings não pode acessar um indice e mudar o valor dele

#   +        0     1    2    3       4
#     -      5     4    3     2      1
lista = ['luiz', 20, True, 1.68, ['gustavo']]
print('lista original: ')
print(lista)

print('lista com valores de indices alterados: ')
lista[-5] = 'joão'
lista[-4] = 40
lista[-3] = False
lista[-2] = 1.85
lista[-1] = 'pedro'
print(lista)