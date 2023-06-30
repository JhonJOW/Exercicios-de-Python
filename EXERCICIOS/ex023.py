ni = int(input('Digite um numero de 1 a 9999: '))
u = ni // 1 % 10
d = ni // 10 % 10
c = ni // 100 % 10
m = ni // 1000 % 10
print('Analisando {}...'.format(ni))
print('Unidade: {}'.format(u))
print('Dezena:  {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:  {}'.format(m))
