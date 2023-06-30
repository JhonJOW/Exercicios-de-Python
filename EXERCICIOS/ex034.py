sa = float(input('Qual é o salário do funcionário? R$'))
au = sa * 15 / 100
if sa >= 1250.00:
    au = sa * 10 / 100
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sa, sa + au))
