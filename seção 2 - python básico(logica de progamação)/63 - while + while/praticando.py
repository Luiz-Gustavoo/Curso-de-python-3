numero_tentativas = 3

while numero_tentativas > 0:
    print('vamos começar nosso teste')
    print(f'você tem mais {numero_tentativas} tentativas')

    pergunta1 = int(input('quanto é 2 + 2?: '))
    resposta_pergunta1 = 4

    if pergunta1 == resposta_pergunta1:
        print('você acertou')
        break
    else:
        print('você errou')
        numero_tentativas -=1

    if numero_tentativas <= 0:
        print('suas tentativas acabaram')

