distan = float(input('Qual é a distancia da sua viagem? '))
if distan <= 200:
    preco = distan * 0.50
else:
    preco = distan * 0.45
print('O preço da sua viagem será de {:.2f}R$'.format(preco))