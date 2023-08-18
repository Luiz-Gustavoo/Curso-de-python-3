def soma(*args):
    total_soma = 0
    for numeros in args:
        total_soma += numeros
    print(total_soma)
soma(1, 2, 3)

def soma_2(*args):
    total_soma = 0
    for numeros in args:
        total_soma += numeros
    return total_soma
soma2_var = soma_2(1, 2, 3)
print(soma2_var)

numeros = 1, 2, 3, 4, 5
print(sum(numeros))
