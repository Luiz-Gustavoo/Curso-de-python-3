"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
CPF: 74682489070
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

# int não é iterável
CPF = '36450622973'
# CALCULANDO O SEGUNDO DÍGITO
contagem_regressiva = 10
soma_resultado_multiplicacao = 0

for digitos in CPF:
    # convertendo para int para ser multiplicado
    digitos_int = int(digitos)

    if contagem_regressiva >= 2:
        # cada digito do cpf * contagem regressiva
        resultado_multiplicacao = 0
        resultado_multiplicacao = digitos_int * contagem_regressiva
        contagem_regressiva -= 1

        # somando os resultados das multiplicações
        soma_resultado_multiplicacao += resultado_multiplicacao
    else:
        break

# multiplicando o resultado da soma das multiplicações
soma_resultado_multiplicado = soma_resultado_multiplicacao * 10

# obter resto da divisão do resultado da soma multiplicado
resto_soma_resultado = soma_resultado_multiplicado % 11

# calculando se o resultado do resto é válido
if resto_soma_resultado <= 9:
    primeiro_digito = resto_soma_resultado
    print(f'O primeiro dígito do CPF é: {primeiro_digito}')
else:
    primeiro_digito = 0
    print(f'O primeiro dígito do CPF é: {primeiro_digito}')

# CALCULANDO O SEGUNDO DÍGITO
contagem_regressiva_2 = 11
soma_resultado_multiplicacao_2 = 0
# 10 digitos - 1: pegando até o primeiro digito
cpf_dez_digitos = CPF[:10]

for digitos in cpf_dez_digitos:
    #  cada digito * contagem regressiva e somando o resultado das multiplicações
    soma_resultado_multiplicacao_2  += (int(digitos) * contagem_regressiva_2)
    contagem_regressiva_2 -=1    

# multiplicando o resultado da soma e pegando o resto dele
segundo_digito = (soma_resultado_multiplicacao_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

print(f'O segundo digito do CPF é : {segundo_digito}')

# validando o CPF digitado com o gerado pelo sistema
cpf_gerado_pelo_sistema = f'{CPF[:9]}{primeiro_digito}{segundo_digito}'
print(f'CPF gerado pelo sistema: {cpf_gerado_pelo_sistema}')

if CPF == cpf_gerado_pelo_sistema:
    print(f'{CPF} é válido')
else:
    print(f'{CPF} é inválido')