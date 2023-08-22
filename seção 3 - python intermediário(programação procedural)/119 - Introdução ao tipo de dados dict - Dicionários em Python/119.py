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

print(pessoa['nome'])
print(pessoa['endereços'])

for dados in pessoa:
    print(pessoa[dados])

