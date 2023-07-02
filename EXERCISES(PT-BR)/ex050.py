s = 0
c = 0
for j in range(1, 7):
    numeros = int(input('Digite o {}° Número Inteiro: '.format(j)))
    if numeros % 2 == 0:
        s += numeros
        c += 1
print('Você informou {} números pares e a soma foi {}.'.format(c, s))