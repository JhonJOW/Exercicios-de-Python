import random
a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceiro nome: ')
a4 = input('Quarto nome: ')
lt = [a1, a2, a3, a4]
print('A pessoa sorteada foi: {}'.format(random.choice(lt)))
