un18_Sum = males_Sum = femaleun20_Sum = 0
proceed_Ask = 'YES'
print(17*'-'+f'\nREGISTER A PERSON\n'+17*'-')
while proceed_Ask.strip().upper() in 'YES':
    age_Ask = int(input('Age: '))
    gender_Ask = str(input(f'Gender[M/F]: '))
    print(17*'-')
    if age_Ask < 18: un18_Sum =+ 1
    if gender_Ask.strip().upper() == 'M': males_Sum =+ 1
    if age_Ask < 20 and gender_Ask.strip().upper() == 'F': femaleun20_Sum =+ 1
    proceed_Ask = str(input('New register[Y/N]? '))
    print(17*'-')
print(f'{males_Sum} males;\n{un18_Sum} under 18 years;\n{femaleun20_Sum} famales under 20 years')
