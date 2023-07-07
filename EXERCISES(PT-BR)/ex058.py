from random import randint
from time import sleep
num = randint(0, 100)
tentativas = 1
print('Adivinhe o número de 0 a 100!')
palpite = int(input('Qual seu palpite? '))
while palpite != num:
    if palpite < num:
        palpite = int(input('Mais... Qual seu palpite? '))
        tentativas += 1
    else:
        palpite = int(input('Menos... Qual seu palpite? '))
        tentativas += 1
print('Acertou!!!')
if tentativas == 1:
    print('Foi de primeira!')
else:
    print('Você usou {} tentativas'.format(tentativas))
