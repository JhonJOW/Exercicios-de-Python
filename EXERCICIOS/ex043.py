peso = float(input('Qual seu peso?  (kg):'))
alto = float(input('Qual sua altura? (m):'))
IMC = peso / alto
print('O IMC dessa pessoa é de {:.0f}!'.format(IMC))
if IMC > 40:
    print('Você está em Obesidade Mórbida, cuidado!')
elif IMC > 30:
    print('Você está em Obesidade.')
elif IMC > 25:
    print('Você está em Sobrepeso.')
elif IMC > 18.5:
    print('Parabéns! Você esta em Peso Ideal.')
elif IMC > 0:
    print('Você está em Abaixo do Peso.')
else:
    print('IMC Ínvalido.')
