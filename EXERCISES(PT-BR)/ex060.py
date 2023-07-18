from math import factorial

num = int(input('Digite um número para\ncalcular seu fatorial: '))
result = factorial(num)
print('{}! = '.format(num), end='')
while num != 0:
    print(num, end='')
    if num != 1:
        print(' x ', end='')
    else:
        print(' =', result)
    num -= 1
    