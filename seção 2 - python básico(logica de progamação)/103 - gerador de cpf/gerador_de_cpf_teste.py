import random
CPF =''
for numeros in range(9):
    CPF += str(random.randint(0, 9))


# CALCULANDO O PRIMEIRO DÍGITO
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
if resto_soma_resultado > 9:
    primeiro_digito = 0
    print(f'O primeiro dígito do CPF é: {primeiro_digito}')
else:
    primeiro_digito = resto_soma_resultado
    print(f'O primeiro dígito do CPF é: {primeiro_digito}')

# CALCULANDO O SEGUNDO DÍGITO
contagem_regressiva_2 = 11
soma_resultado_multiplicacao_2 = 0
# 10 digitos - 1: pegando até o primeiro digito
cpf_dez_digitos = CPF[10]

for digitos in cpf_dez_digitos:
    #  cada digito * contagem regressiva e somando o resultado das multiplicações
    soma_resultado_multiplicacao_2  += (int(digitos) * contagem_regressiva_2)
    contagem_regressiva_2 -=1    

# multiplicando o resultado da soma e pegando o resto dele
segundo_digito = (soma_resultado_multiplicacao_2 * 10) % 11
segundo_digito = 0 if segundo_digito > 9 else segundo_digito

print(f'O segundo digito do CPF é : {segundo_digito}')

# validando o CPF digitado com o gerado pelo sistema
cpf_gerado_pelo_sistema = f'{CPF}{primeiro_digito}{segundo_digito}'
print(cpf_gerado_pelo_sistema)

if CPF == cpf_gerado_pelo_sistema:
    print(f'{CPF} é válido')
else:
    print(f'{CPF} é inválido')