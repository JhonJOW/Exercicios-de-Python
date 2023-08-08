num1 = int(input('Type a number: '))
num2 = 0 # the avarge
num3 = 1 # how many numbers typed
num4 = num1 # higher number
num5 = num1 # lower number
num6 = num1 # previous number
num2 += num1
ask1 = str(input('Want to continue? [Y/N] ')).upper().strip()

while ask1 == 'Y':
    ask1 = 'N'
    num3 += 1
    num1 = int(input('Type a number: '))
    num2 += num1
    ask1 = str(input('Want to continue? [Y/N] ')).upper().strip()
    if num1 < num6:
        num5 = num1
    elif num1 > num6:
        num4 = num1
    num6 = num1

print('You typed {} numbers and their average was {}.'.format(num3, num2 / num3))
print(f'The highest number was {num4} and the lower {num5}.')
