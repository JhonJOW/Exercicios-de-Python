from random import randint
print('\033[33m-=-\033[m' * 12)
print('\033[36;1m       Acerte o Número!!!\033[m')
print('\033[33m-=-\033[m' * 12)
start = str(input(' \033[36;4mFácil\033[m(a) / \033[31;4mDifícil\033[m(b): '))
if start == 'a':
    comp1 = randint(1, 3)
    n1 = int(input('Digite um número de \033[33m1\033[m a \033[33m3\033[m: '))
    if n1 == comp1:
        print('\033[32;1mVOCÊ ACERTOU, PARABÉNS!!!\033[m')
    else:
        print('\033[31;1mErrou!\033[m')
        print('O número era: {}{}{}'.format('\033[31;1m', comp1, '\033[m'))
else:
    comp2 = randint(1, 10)
    n2 = int(input('Digite um número de \033[33m1\033[m a \033[33m10\033[m: '))
    if n2 == comp2:
        print('\033[32;1mVOCÊ ACERTOU, PARABÉNS!!!\033[m')
    else:
        print('\033[31;1mErrou!\033[m')
        print('O número era: {}{}{}'.format('\033[31;1m', comp2, '\033[m'))
print('\033[33m-=--=--=--=--=--FIM!--=--=--=--=--=-\033[m')
