# sem adiar passar parâmetro
def criar_soma(x, y):
    def soma():
        return x + y
    return soma

somar_1 = criar_soma(2, 2)
print(somar_1())


# adiar passar parâmetro

def criar_soma_2(x):
    def soma_2(y):
        return x + y
    return soma_2

somar_2 = criar_soma_2(4)
print(somar_2(5))
