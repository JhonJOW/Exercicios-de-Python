number_List = []
for x in range(5):
    number_Ask = int(input(f'Type a number for position {x + 1}: '))
    number_List.append(number_Ask)
print(f'You typed: {number_List}')
if number_List.count(max(number_List)) == 5:
    print('All the position has the same value.')
else:
    biggest_Quant = number_List.count(max(number_List))
    smallest_Quant = number_List.count(min(number_List))
    print(f'The biggest number was {max(number_List)} on position ', end='')
    actual_Num = 0
    while biggest_Quant > 0:
        print(f'{number_List.index(max(number_List), actual_Num) + 1}... ', end='')
        actual_Num = (number_List.index(max(number_List), actual_Num) + 1)
        biggest_Quant -= 1
    print(f'\nThe smallest number was {min(number_List)} on position ', end='')
    actual_Num = 0
    while smallest_Quant > 0:
        print(f'{number_List.index(min(number_List), actual_Num) + 1}... ', end='')
        actual_Num = (number_List.index(min(number_List), actual_Num) + 1)
        smallest_Quant -= 1
