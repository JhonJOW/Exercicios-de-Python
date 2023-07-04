idadeanterior = 0
menores = 0
velhonome = str
velhoidade = 0
for j in range(0, 4):
    print('----- {}ª PESSOA -----'.format(j + 1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    idadeanterior += idade
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if sexo == 'F' and idade < 20:
        menores += 1
    if sexo == 'M' and idade > velhoidade:
        velhoidade = idade 
        velhonome = nome

print('A média de idade do grupo é de {:.1f} anos.'.format(idadeanterior / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velhoidade, velhonome))
print('Ao todo são {} mulher(s) com menos de 20 anos.'.format(menores))