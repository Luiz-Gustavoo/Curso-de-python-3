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

palavra_secreta = 'computador'
palavra_formatada = ''
numero_tentativa = 0

print('                         JOGO DA PALAVRA SECRETA                                ')
print('                 tente adivinhar a palavra letra por letra                      ')
print('-'* 100)

for letras in palavra_secreta:
    input_letra = input('digite uma letra: ')

    if input_letra in palavra_secreta:
        palavra_formatada += input_letra
        print(input_letra)
    
    else:
        print('letra errada')
        palavra_formatada = '*' * len(palavra_secreta)
        print(palavra_formatada)
        continue
      
else:
    print('você adivinhou a palavra secreta')
    print(palavra_formatada)