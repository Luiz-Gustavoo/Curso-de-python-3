"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'computador'
letras_acertadas = ''



print('                         JOGO DA PALAVRA SECRETA                                ')
print('                 tente adivinhar a palavra letra por letra                      ')
print('-'* 100)

while True:
        input_letra = str(input('digite uma letra: '))

        if len(input_letra) > 1:
            print('digite apenas uma letra')
            continue

        if input_letra in palavra_secreta:
              letras_acertadas += input_letra
            
        palavra_formada = ''
        for letra_secreta in palavra_secreta: 
              if letra_secreta in letras_acertadas: # vai rodar letra por letra da palavra secreta até achar as que estão acertadas pelo usuario
                    palavra_formada += letra_secreta     
              else:
                palavra_formada += "*"

        print(palavra_formada)
        

        if palavra_formada == palavra_secreta:
             os.system('cls')
             print('VOCÊ ACERTOU A PALAVRA!')
             print("A palavra secreta era {}".format(palavra_secreta))