from random import randint
x = [randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)]
for y in x:
    print(y, end='')
print('\nThe biggest number is ', max(x))
print('The smallest number is ', min(x))
