
number_Lst = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
              'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 
              'Nineteen', 'Twenty')
while True:
    number_Ask = int(input('Type a number between 0 and 20: '))
    if -1 < number_Ask < 20:
        print(f'You typed {number_Ask}, in words is {number_Lst[number_Ask]}')
        break
    else:
        print('INVALID NUMBER! ', end='')