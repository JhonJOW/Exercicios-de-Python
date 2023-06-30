word = str(input('Digite uma frase: ')).strip().upper()
frase = word.split()
together = ''.join(frase)
reverse = ''
for letter in range(len(together) - 1, -1, -1):
    reverse += together[letter]
print('O inverso de {} é {}'.format(together, reverse))
if together == reverse:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
