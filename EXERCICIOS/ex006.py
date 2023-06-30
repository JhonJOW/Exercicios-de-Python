n1 = int(input('1° Valor: '))
n2 = int(input('2° Valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rs = n1 % n2
print('A soma é {}, a subtração é {}, o produto é {} e a divisão é {:.3f}.'.format(a, s, m, d), end=' ')
print('A divisão inteira dá {} e fica com o resto de {}.'.format(di, rs))
