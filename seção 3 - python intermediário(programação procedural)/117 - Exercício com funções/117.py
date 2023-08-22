# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def manipular_numero(numero): # parametro função externa (vai ficar salvo na memória)
    def manipulador(numero_alterador): # parametro função interna
        if numero_alterador == 2:
            return numero * 2
        elif numero_alterador == 3:
            return numero * 3
        elif numero_alterador == 4:
            return numero * 4
    return manipulador
        
chamando_manipular_numero = manipular_numero(2) # passando parâmetro externo (número que será alterado)
print(chamando_manipular_numero(4)) # passando parâmetro interno (número que ir multiplicar o que será alterado)
