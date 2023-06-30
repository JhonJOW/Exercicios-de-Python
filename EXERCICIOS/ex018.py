from math import hypot
co = float(input('Qual o comprimento do cateto oposto?: '))
ca = float(input('Qual o comprimento do cateto adjacente?: '))
hi = hypot(co, ca)
print('Hipotenusa: {:.2f}'.format(hi))
