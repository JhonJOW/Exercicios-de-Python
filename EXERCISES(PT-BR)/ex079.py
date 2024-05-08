num_List = list()
while True:
    num_Digt = int(input('Type a value: '))
    if num_Digt not in num_List:
        num_List.append(num_Digt)
    else:
        print('That value was been already added!')
    ask_Cfrm = str(input('Want to continue? [S/N]: ')).upper()
    if ask_Cfrm == 'N':
        break
num_List.sort()
print(num_List)