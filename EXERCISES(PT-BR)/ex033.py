n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
if n1 == n2 and n1 == n3:
    print('Todos tem o mesmo valor!')
else:
    mn = n1
    if n2 < n1:
        mn = n2
    if n3 < n2 and n3 < n1:
        mn = n3
    mr = n1
    if n2 > n1:
        mr = n2
    if n3 > n2 and n3 > n1:
        mr = n3
    print('O menor número é {} e o maior é {}!'.format(mn, mr))
