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
     #             0123456789
palavra_secreta = 'computador'
indice_palavra_secreta = 0
palavra_formatada = ''
indice_palavra_formatada = 0


print('                         JOGO DA PALAVRA SECRETA                                ')
print('                 tente adivinhar a palavra letra por letra                      ')
print('-'* 100)

for letras in palavra_secreta:
    input_letra = str(input('digite uma letra: '))

    if input_letra in palavra_secreta:
        palavra_formatada += input_letra
else:
    print(palavra_formatada)        