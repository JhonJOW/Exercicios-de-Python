larg = float(input('qual a largura (em metros) da superfície que você irá pintar?\nR: '))
alt = float(input('qual a altura (em metros) da superfície que você irá pintar?\nR: '))
ar = larg * alt
print('Você precisará de {:.1f}l de tinta para pintar a superfície.'.format(ar / 2))
