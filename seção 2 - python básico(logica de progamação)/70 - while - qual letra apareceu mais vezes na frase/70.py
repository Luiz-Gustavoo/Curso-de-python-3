frase = 'laaa'

contador_indice = 0
qtd_apareceu_mais = 0
letra_apareceu_mais = ''

while contador_indice < len(frase):
    letra_atual = frase[contador_indice]

    if letra_atual == ' ':
        contador_indice+=1
        continue

    quantas_vezez_apareceu = frase.count(letra_atual)

    if qtd_apareceu_mais < quantas_vezez_apareceu:
        letra_apareceu_mais = letra_atual
        qtd_apareceu_mais = quantas_vezez_apareceu
        
    
    contador_indice+=1
        
    

print(letra_apareceu_mais)
