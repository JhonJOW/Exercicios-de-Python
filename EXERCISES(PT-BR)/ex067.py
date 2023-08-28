num2 = num1 = 1

while True:
    print(38*'-')
    num1 = int(input('Want to see the table of which number: '))
    print(38*'-')
    if num1 < 1: break
    for j in range(1, 11):
        print(f'{num1} x {j:2} = {j*num1}')
print('Program fineshed, come back anytime!')