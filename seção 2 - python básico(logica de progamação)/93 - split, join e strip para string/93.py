"""
método split: divide uma string em determnidado caractere
    - caso não tenha um parâmetro, vai separar nos espaços
    - retorna uma lista

método strip: corta espaços em uma string
"""

frase = '    Olha só   , que coisa interessante'
print(frase)

frase_separada = frase.split(',')
print(frase_separada)

frase_separada_nova = []
for i, frase in enumerate(frase_separada):
    # corrigindo os espaços da variável frase_separada
    frase_separada_nova.append(frase_separada[i].strip())
print(frase_separada_nova)


frases_unidas = ', '.join(frase_separada_nova)
print(frases_unidas)