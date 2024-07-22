num_List = []
for j in range(0, 5):
    num_Digit = int(input("Type a value: "))
    if j == 0 or num_Digit > num_List[-1]:
        num_List.append(num_Digit)
        print(f"The value {num_Digit} was placed in {j} position.")
    else:
        list_Position = 0
        while list_Position < len(num_List):
            if num_Digit <= num_List[list_Position]:
                num_List.insert(list_Position, num_Digit)
                print(f"The value {num_Digit} was placed in {list_Position} position.")
                break
            list_Position += 1
            
print(f"The typed values were {num_List}.")