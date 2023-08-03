num1 = int(input('Type a number [999 to stop]: '))
num2 = 0
num3 = 0
while num1 != 999:
    num2 += 1
    num3 += num1
    num1 = int(input('Type a number [999 to stop]: '))
print('The total of numbers typed is {} and the sum of it is {}.'.format(num2, num3))
