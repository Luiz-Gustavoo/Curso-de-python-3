# iterando com while: usado quando não se sabe quantas repetições vão exister
nome = 'luiz gustavo'

contador = 0

while contador < len(nome):
    print(nome[contador])
    contador+=1


# for: estrutura de repetição para coisas finitas(iteração)

print(30 * '-')    

nome2 = 'luiz gustavo'

for letras in nome2: # a variavel "letra" é aonde os elementos da variavel "nome2" são adicionados
    print(letras)