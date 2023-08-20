# função como parâmetro de outra função teste

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa_saudacao(funcao, msg, *args): #coloca os parâmetros passados na chamada em uma tupla
    return funcao(msg, *args)   # desempacotou os argumentos que estavam na tupla

print(executa_saudacao(saudacao, 'Bom dia', 'Luiz'))

print(executa_saudacao(saudacao, 'Boa tarde', 'João'))
