from random import shuffle
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lt = [n1, n2, n3, n4]
random.shuffle(lt)
print('A Sequência de apresentação é: {}'.format(lt))
