"""
desempacotamento: colocar os valores de uma lista em uma váriavel
"""

nomes = ['maria', 'luiz', 'helena']

nome1, nome2, nome3 =nomes
print(nome1)

"""
quando se deseja desempacotar somente 1 valor de uma lista,
precisa colocar o resto dos valores
em uma váriavel(essa váriavel vai ser usada)
"""

nomes2 = ['maria', 'luiz', 'helena']

nome_1, *resto = nomes
print(nome_1, resto)

"""
quando se deseja desempacotar somente 1 valor de uma lista,
precisa colocar o resto dos valores
em uma váriavel(essa váriavel não vai ser usada)
"""

nomes2 = ['maria', 'luiz', 'helena']

_, nome_02, *_ = nomes
print(nome_02)