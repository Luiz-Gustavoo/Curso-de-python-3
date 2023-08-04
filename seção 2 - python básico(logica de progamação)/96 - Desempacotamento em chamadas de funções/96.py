lista_nomes = ['luiz', 'helena', 'pedro', 'mateus']

nome1, nome2, nome3, *_ = lista_nomes
print(nome1, nome2, nome3)

print('')

for nomes in lista_nomes:
    print(nomes,end=', ') # printando os nomes em uma linha

print('')

print(*lista_nomes) # desempacotando no print