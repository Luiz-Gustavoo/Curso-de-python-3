import random
"""
método randint(gera um número inteiro aleatório entre dois números)
"""
cpf =''
for numeros in range(9):
    cpf += str(random.randint(0, 9))

# CALCULANDO O PRIMEIRO DÍGITO
contagem_regressiva = 10

soma_resultado_multiplicacao = 0
for digitos in cpf:
    # convertendo para int para ser multiplicado
    digitos_int = int(digitos)

    if contagem_regressiva >= 2:
        # cada digito do cpf * contagem regressiva
        resultado_multiplicacao = 0
        resultado_multiplicacao = digitos_int * contagem_regressiva
        contagem_regressiva -= 1

        # somando os resultados das multiplicações
        soma_resultado_multiplicacao += resultado_multiplicacao

        # multiplicando o resultado da soma das multiplicações
        soma_resultado_multiplicado = soma_resultado_multiplicacao * 10

    # obter resto da divisão do resultado da soma multiplicado
        resto_soma_resultado = soma_resultado_multiplicado % 11

    # calculando se o resultado do resto é válido
        if resto_soma_resultado <= 9:
            primeiro_digito = resto_soma_resultado
            
        else:
            primeiro_digito = 0
            
    else:
        break

    
# CALCULANDO O SEGUNDO DÍGITO
contagem_regressiva_2 = 11
soma_resultado_multiplicacao_2 = 0
# 10 digitos - 1: pegando até o primeiro digito
cpf_dez_digitos = cpf + str(primeiro_digito)

for digitos in cpf_dez_digitos:
    #  cada digito * contagem regressiva e somando o resultado das multiplicações
    soma_resultado_multiplicacao_2  += (int(digitos) * contagem_regressiva_2)
    contagem_regressiva_2 -=1    

    # multiplicando o resultado da soma e pegando o resto dele
    segundo_digito = (soma_resultado_multiplicacao_2 * 10) % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0

print(f'O primeiro dígito do CPF é: {primeiro_digito}')
print(f'O segundo digito do CPF é : {segundo_digito}')

# validando o CPF digitado com o gerado pelo sistema
cpf_gerado_pelo_sistema = f'{cpf}{primeiro_digito}{segundo_digito}'
print(f'CPF gerado pelo sistema: {cpf_gerado_pelo_sistema}')

if cpf == cpf_gerado_pelo_sistema:
    print(f'{cpf} é válido')
else:
    print(f'{cpf} é inválido')

