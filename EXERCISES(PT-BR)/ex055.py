maior = 0
menor = 0
pesoanterior = 0
for j in range(0, 5):
    pesoatual = float(input('Peso da {}ª Pessoa: '.format(j + 1)))
    if j == 0:
        maior = pesoatual
        menor = pesoatual
    else:
        if pesoatual < menor:
            menor = pesoatual
        elif pesoatual > maior:
            maior = pesoatual
    pesoanterior = pesoatual
print('O maior peso lido foi {}Kg e o menor foi {}Kg.'.format(maior, menor))
