pessoa = {
    'nome': 'luiz gustavo',
    'sobrenome': 'zanerato',

}
print(len(pessoa))

print(list(pessoa.keys()))

print(list(pessoa.values()))

print(list(pessoa.items()))

for chave, valor in pessoa.items():
    print(chave, valor)


pessoa.setdefault('idade', 21)
print(pessoa['idade'])
