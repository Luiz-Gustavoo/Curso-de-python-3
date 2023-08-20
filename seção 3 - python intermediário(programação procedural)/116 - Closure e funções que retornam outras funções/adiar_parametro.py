def criar_saudacao(saudacao): # função externa
    def saudar(nome): # função interna
        return f'{saudacao}, {nome}!'
    return saudar

saudar_1 = criar_saudacao('Bom dia') # variavel que chama a função externa e passa seu parâmetro
print(saudar_1('Luiz')) # print da chamada da função, mas com o parâmetro da função interna, já que o parametro da função externa está armazenado

