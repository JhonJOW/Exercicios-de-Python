num = int(input('Digite um valor: '))
tot = 0
for j in range(1, num + 1):
    if num % j == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(j), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('Então ele é Primo.'.format(num))
else:
    print('Então ele não é Primo'.format(num))