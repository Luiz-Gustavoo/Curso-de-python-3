# or: ou
# só precisa de uma condição verdeira para a expressão ser verdadeira
senha_digitada = input('digite sua senha: ') or 'não digitou a senha'
senha_certa = "123"

entrar_sair = input('digite [E] para entrar ou [S] para sair ')

if (entrar_sair == 'E' or 'e') and senha_digitada == senha_certa:  # tudo dentro de parênteses é avaliado primeiro
    print('você entrou')

elif entrar_sair == "S":
    print('você saiu')