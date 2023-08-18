"""
Exercícios com funções
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável.
"""
def multiplicacao(*args):
    total_multiplicacao = 1
    for numeros in args:
        for numero_corretos in numeros:  
            total_multiplicacao *= numero_corretos
    return total_multiplicacao

numeros_multiplicar = []
while True:
    input_numeros = input('Digite um número: ')
    input_numeros_formatado = int(input_numeros)
    numeros_multiplicar.append(input_numeros_formatado)
    adicionar_mais_numeros = input('Deseja adicionar mais números? [s]im [n]]ão: ')
    if adicionar_mais_numeros == 's':
        continue
    elif adicionar_mais_numeros == 'n':
        break

chamada_multiplicacao = multiplicacao(numeros_multiplicar)
print(f'O total da multiplicação entre: {numeros_multiplicar} é: {chamada_multiplicacao}')
