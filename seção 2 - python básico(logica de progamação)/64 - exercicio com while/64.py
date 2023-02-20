"""
iterando uma string com while
"""
#       01234567891011
nome = 'luiz gustavo'
contador_indice = 0
nome_formatado = ''


while contador_indice < len(nome):
    letra = nome[contador_indice]
    nome_formatado += f'-{letra} '
    
    contador_indice +=1
    
print(nome_formatado)    
    
'''
nome = 'luiz'
novo_nome = ''
contador = 0

while contador < len((nome)):
    letra = nome[contador]
    print(letra)
    contador+=1
    novo_nome +=f'*{letra}'
print(novo_nome)
'''

