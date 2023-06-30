casa = int(input('Qual o valor da casa:        R$'))
din = int(input('Salário do comprador:        R$'))
anos = int(input('Quantos anos de financiamento? '))
div = casa / (anos * 12)
print('Para pagar a casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}.'.format(casa, anos, div))
if div <= (din / 100 * 30):
    print('Empréstimo pode ser \033[32mCONCEDIDO\033[m!')
else:
    print('Empréstimo \033[31mNEGADO\033[m!')
