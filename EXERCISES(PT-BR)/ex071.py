print('Wells Fargo')
withdraw_Ask = int(input('How much money you want to withdraw? US$ '))
if withdraw_Ask / 50 != float:
    print('50 banknote: {:.0f}'.format(withdraw_Ask / 50))
    rest_Sum = withdraw_Ask % 50
if rest_Sum / 20 != float or rest_Sum != 0:
    print('20 banknote: {:.0f}'.format(rest_Sum / 20))
    rest_Sum = (withdraw_Ask % 50) % 20
if rest_Sum / 10 != float or rest_Sum != 0:
    print('10 banknote: {:.0f}'.format(rest_Sum / 10))
    rest_Sum = ((withdraw_Ask % 50) % 20) % 10
if rest_Sum / 5 != float or rest_Sum != 0:
    print('5 banknote: {:.0f}'.format(rest_Sum / 5))
    rest_Sum = (((withdraw_Ask % 50) % 20) % 10) % 5
if rest_Sum / 1 != float or rest_Sum != 0:
    print('1 banknote: {:.0f}'.format(rest_Sum / 1))
