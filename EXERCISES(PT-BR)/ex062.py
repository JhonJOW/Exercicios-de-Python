print('GERADOR DE P.A.\n',6*'=-=')

cont1 = 0
cont2 = 1
termo = int(input('Primeiro termo: '))
razao = int(input('Razão   da  PA: '))

while cont2 > 0:
    while cont1 < 9:
        cont1 += 1
        print(termo, '➝  ', end='')
        termo += razao
    while cont2 > 0:
        cont1 += 1
        cont2 -= 1
        print(termo, '➝  ', end='')
        termo += razao
    print('PAUSA')
    cont2 = int(input('Quantos termos você quer mostrar a mais? '))
print('Progreção finalizada com {} termos mostrados.'.format(cont1))
