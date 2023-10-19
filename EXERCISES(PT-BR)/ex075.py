count = 0
x = int(input('Type a number: ')), int(input('Type a number: ')), int(input('Type a number: ')), int(input('Type a number: '))
print(f'The number 9 appeared {x.count(9)} time(s).')
if 3 in x:
    print(f'The number 3 appeared on position {x.index(3)+1}.')
for y in x:
    if y % 2 == 0:
        count += 1
print(f'Pair numbers appeared {count} time(s).')
