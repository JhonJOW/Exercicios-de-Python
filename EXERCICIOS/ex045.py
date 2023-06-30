from random import randint
from time import sleep
items = ('pedra', 'papel', 'tesoura')
print('''Suas Opções:
[1] Pedra
[2] Papel
[3] Tesoura''')
comp = randint(0, 2)
user = int(input('Qual sua escolha? ')) - 1
sleep(1)
print('\033[33mJO !')
sleep(2)
print('KEN!')
sleep(2)
print('PO !\033[m')
sleep(0.5)
print('-='*13)
print('O Computador jogou {}'.format(items[comp]))
print('O  Jogador  jogou  {}'.format(items[user]))
print('-='*13)
if comp == 0:  # Computador jogou PEDRA
    if user == 0:  # Contra Pedra
        print('          Impate')
    elif user == 1:  # Contra Papel
        print('          Vitória')
    else:  # Contra Tesoura
        print('          Derrota')
elif comp == 1:  # Computador jogou PAPEL
    if user == 0:  # Contra Pedra
        print('          Derrota')
    elif user == 1:  # Contra Papel
        print('          Impate')
    else:  # Contra Tesoura
        print('          Vitória')
else:  # Computador jogou TESOURA
    if user == 0:  # Contra Pedra
        print('          Vitória')
    elif user == 1:  # Contra Papel
        print('          Derrota')
    else:  # Contra Tesoura
        print('          Impate')
