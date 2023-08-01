

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2

#vai gerar um resultado impreciso
print(numero3)

#contornando a imprecisão: f string e redução de casas decimais
print(f'{numero3:.2f}')

#contornando a imprecisão: função round
print(round(numero3, 2))

#contornando a imprecisão: módulo decimal
