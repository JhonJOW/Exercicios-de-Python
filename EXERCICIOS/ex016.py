km = float(input('Quantos Km rodados?\nR: '))
ds = int(input('Quantos dias alugados?\nR: '))
dinkm = km * 15 / 100
dinds = ds * 60
print('O total a pagar é de R${:.2f}'.format(dinkm + dinds))
