def criar_saudacao(saudacao, nome): # função externa
    def saudar(): # função interna
        return f'{saudacao}, {nome}!'
    return saudar

saudar_1 = criar_saudacao('Bom dia', 'Pedro')
print(saudar_1())
