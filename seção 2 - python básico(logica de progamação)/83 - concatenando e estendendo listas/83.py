# polimorfismo: sinal se comporta de outra maneira com certo tipo de dado

# concatenando lista

lista_a = [1, 2, 3, 4]
lista_b = [5, 6, 7, 8]
lista_c = lista_a + lista_b

print(lista_c)

# extend
lista_d = lista_a.extend(lista_b)
print(lista_d)
print(lista_a)