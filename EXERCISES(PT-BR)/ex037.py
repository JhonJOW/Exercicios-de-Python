n = int(input('Digite um número: '))
print('[1] Para converção de OCTAL')
print('[2] Para converção de BINÁRIO')
print('[3] Para converção de HEXADECIMAL')
esco = int(input('Para qual linguagem você deseja converter? '))
if esco == 1:
    print('O número {} convertido para OCTAL vira: {}'.format(n, oct(n)))
elif esco == 2:
    print('O número {} convertido para BINÁRIO vira: {}'.format(n, bin(n)))
elif esco == 3:
    print('O número {} convertido para HEXADECIMAL vira {}'.format(n, hex(n)))
else:
    print('Você é bobo ou quer 2 conto? \033[31mOPÇÃO INVALIDA!\033[m')
