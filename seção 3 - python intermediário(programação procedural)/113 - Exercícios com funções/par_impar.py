"""
crie uma função que retorne se o número é ímpar ou par
"""

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    return f' {numero} é par' if multiplo_de_dois else f'{numero} é Ímpar'
    
chamar_par_impar = par_impar(5)
print(chamar_par_impar)
