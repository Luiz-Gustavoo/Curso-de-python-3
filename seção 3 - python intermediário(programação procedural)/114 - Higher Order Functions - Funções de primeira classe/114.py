# variável apontando para função
def saudacao(msg):
    return msg

print(saudacao('Boa tarde'))

# função como parâmetro de outra função

def soma(x, y): # soma precisa de x e y para funcionar
    return x + y

def executa_soma(funcao, x, y): # recebe soma e os parâmetros de soma como parâmetro
    return funcao(x, y)

chamando_executa_soma = executa_soma(soma, 2, 4) # passando soma como parâmetro e os parâmetros da própria soma
print(chamando_executa_soma)
