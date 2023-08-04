"""
operação ternária: condicional de uma linha
"""

condicao_maioridade = 18
idade = 'Maior de idade' if condicao_maioridade else 'Menor de idade'
print(idade)

print('')

digito = 9
#            se digito for >= 0 e <= 9, o valor de digito será atribuído a novo_digito
novo_digito = digito if digito >= 0 and digito <= 9 else 0
print(novo_digito)