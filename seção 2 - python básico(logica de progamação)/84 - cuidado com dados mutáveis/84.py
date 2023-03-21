"""
imutaveis: copia o valor de uma variavel para outra
"""
nome = 'luiz'
nome = 'gustavo'
print(nome)

"""
mutavel: as duas variaveis apontam para o mesmo valor
        quando altera uma, altera na outra também
"""

lista_a = ['banana', 'maçã', 'laranja']

# copiando lista
lista_d = lista_a.copy()
print(lista_d)

# apontando
lista_b = lista_a

lista_b[0] = 'morango'

print(lista_a)

