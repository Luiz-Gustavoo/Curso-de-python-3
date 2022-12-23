primeiro_numero = input('digite um número: ')
primeiro_int = int(primeiro_numero)
segundo_numero = input('digite outro número: ')
segundo_int = int(segundo_numero)

if primeiro_int > segundo_int:
    print('primeiro número = "{}" é maior do que o segundo número = "{}"'.format(primeiro_int, segundo_int))
elif segundo_int > primeiro_int:
    print('segundo número = "{}" é maior do que o primeiro número = "{}"'.format(segundo_int, primeiro_int))


    