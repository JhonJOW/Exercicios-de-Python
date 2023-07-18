print(6*' ','GERADOR DE P.A.\n',9 * '=-=')
x = 0
termo = int(input('Primeiro termo: '))
razao = int(input('Razão   da  PA: '))
while x < 10:
    x += 1
    print(termo, '➝  ', end='')
    termo += razao
print('FIM')
