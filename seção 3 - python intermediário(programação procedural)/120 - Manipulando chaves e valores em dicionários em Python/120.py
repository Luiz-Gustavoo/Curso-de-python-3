pessoa = {
    'nome': 'Luiz gustavo',
    'Sobrenome': 'zanerato',
    'idade': 21,
    'altura': '1.68',
    'endereços': [
        {
            'bairro': 'tal bairro',
            'Rua': 'tal rua',
            'número': 123
        }
    ]
}

pessoa2 = {}
# criando chaves
pessoa2['nome'] = 'luiz gustavo'
print(pessoa2)
#acessando chaves
print(pessoa2['nome'])

# chave dinâmica
chave = 'sobrenome'
pessoa2[chave] = 'zanerato'
print(pessoa2[chave])

# alterar valor de chave

pessoa2['nome'] = 'Maria'
print(pessoa2['nome'])

# apagar chaves
pessoa2['idade'] = 21
print(pessoa2)
del pessoa2['idade']
print(pessoa2)

# acessar chaves que não existem (validar)
try:
    print(pessoa2['idade'])
except:
    print('Esse valor não existe')

print(pessoa2.get('altura', 'Esse valor não existe'))
