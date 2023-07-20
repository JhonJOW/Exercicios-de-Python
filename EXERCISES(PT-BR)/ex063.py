print('    Fibonacci sequence:\n',5*'-----')
n = int(input('How many terms you want? '))
t1 = 0
t2 = 1
t3 = 1
cont = 0
print(' {} ➞  {}'.format(t1, t2), end='')
while cont != (n-2):
    cont += 1
    t3 = t1+t2
    print(' ➞  {}'.format(t3), end='')
    t1 = t2
    t2 = t3
print(' ➞  FIM')