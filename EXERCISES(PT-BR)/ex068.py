from random import randint
gam_Win = 0
gam_Ask = 'YES'
while gam_Ask.upper() in 'YES':
    num_Ask = int(input('Which number? '))
    num_Npc = randint(1, 10)
    num_End = num_Ask+num_Npc
    opt_Ask = str(input('Pair or  odd? ')).strip().upper()
    sum_End = 'Pair' if (num_End%2)==0 else 'Odd'
    print(f'The sum of your {num_Ask} plus bot {num_Npc} is {num_End}. {sum_End}!', end='')
    if opt_Ask in sum_End.upper():
        print(' You win!!!')
        gam_Ask = str(input('Want to retry (Y/N)? '))
        gam_Win =+ 1
    else:
        print(' Game over.')
        break
print(f'You won {gam_Win} consecutive games.')
