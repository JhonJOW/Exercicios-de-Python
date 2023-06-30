pr = float(input('Preço do item? R$'))
dca = pr * 0.05
print('O preço, usando o cupom, irá de {} para {:.2f}.'.format(pr, pr - dca))
