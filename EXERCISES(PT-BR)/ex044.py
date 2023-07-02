print('_-'*3,'LOJA JHONJHON','_-'*3)
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO:')
print('[ 1 ] À vista Dinheiro/Cheque')
print('[ 2 ] À vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if 0 < opcao < 5:
    if opcao == 1:
        conta = preco - (preco * 0.1)
    elif opcao == 2:
        conta = preco - (preco * 0.05)
    elif opcao == 3:
        conta = preco
    elif opcao == 4:
        conta = preco + (preco * 0.2)
        parcelas = int(input('Quantas parcelas? '))
        if parcelas > 12:
            print('Número de parcelas ínvalido.')
        else:
            parcela = conta / parcelas
            print('Sua compra será parcelada em {}x de {} COM JUROS.'.format(parcelas, parcela))
    print('Sua compra de R${} vai custar R${} no final.'.format(preco, conta))
else:
    print('\033[31mOPÇÃO ÍNVALIDA\033[m')