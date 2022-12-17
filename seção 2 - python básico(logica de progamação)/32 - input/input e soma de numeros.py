n1 = input('digite um número: ')
n2 = input('digite um número: ')

int_n1 = int(n1)
int_n2 = int(n2)

print(f'a soma entre os dois números é: {int_n1 + int_n2}')
print('a multiplicação entre os dois números é: {}'.format(int_n1 * int_n2))

if int_n1 % 2 == 0:
    print(f'{int_n1} é divisível por 2')
else:
    print('{} não é divisível por 2'.format(int_n1))    

if int_n2 % 2 == 0:
    print(f'{int_n2} é divisível por 2')
else:
    print('{} não é divisível por 2'.format(int_n2))
    