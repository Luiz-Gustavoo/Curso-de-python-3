# and: e
# as duas condições precisam ser verdeiras para a expressão ser verdadeira
senha_digitada = input('digite sua senha: ')
senha_certa = "123"

entrar_sair = input('digite [E] para entrar ou [S] para sair ')

if entrar_sair == 'E' and senha_digitada == senha_certa:
    print('você entrou')

elif entrar_sair == "S":
    print('você saiu')
