"""
iterando uma string com while
"""
#       01234567891011
nome = 'luiz gustavo'
len_nome = len(nome)
contador_indice = 0


nome_formatado = ''
len_nome_formatado = len(nome_formatado)

while len_nome_formatado < len_nome:
    if len(nome_formatado) == len(nome):
        break
    
    indice_nome = nome[contador_indice]
    nome_formatado += indice_nome
    contador_indice +=1

    if len(nome_formatado) == len(nome):
        print(nome_formatado)
    
    

