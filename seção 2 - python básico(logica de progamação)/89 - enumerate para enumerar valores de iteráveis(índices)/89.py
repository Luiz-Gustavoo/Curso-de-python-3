"""
o enumerate irá colocar os respectivos índices de valores ao lado deles
só pode ser usado uma vez
"""
#           0        1        2
lista = ['maria', 'helena', 'luiz']
lista_enumerada = tuple(enumerate(lista))
print(lista_enumerada[0][1])
#        0              1           2
#   0       1     0     1        0     1
# ((0, 'maria'), (1, 'helena'), (2, 'luiz'))


print('ENUMERATE PADRÃO:')
for valores_enumerados in lista_enumerada:
   print(valores_enumerados)

for valores_enumerados in lista_enumerada:
   print(valores_enumerados)


 #usar o enumerate mais de uma vez: enumerate direto no for

print('ENUMERATE DIRETO NO FOR:')
for valores_enumerados in enumerate(lista):
   print(valores_enumerados)

for valores_enumerados in enumerate(lista):
   print(valores_enumerados)


 #usar o enumerate mais de uma vez: type conversion

print('TYPE CONVERSION:')
lista_enumerada = list(enumerate(lista))
print(lista_enumerada)


for indice, nome in enumerate(lista):
   print(indice, nome)


