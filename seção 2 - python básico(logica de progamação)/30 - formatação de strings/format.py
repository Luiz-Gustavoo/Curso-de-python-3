# objetos: podem realizar ações e essas ações se chamam métodos(funções que fazem alguma coisa)
nome = 'luiz'
idade = 20


format = '{}, {}'.format(nome,idade)  # nome e idade  se tornam argumentos
print(format)

print('------------------')

A = 'arroz'
B = 'feijão'
C = 'suco'
D = 'chocolate'
E = 'frango'
lista = '\n 1 = {}\n 2 = {}\n 3 = {}\n 4 = {}\n 5 = {}'
lista_formatada = lista.format(A, B, C, D, E)

print(lista_formatada)

# erro  out of range: não encontra o valor para tal argumento
