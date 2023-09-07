proceed_Ask = cheapest_Nam = 'Y'
cheapest_Wrt = price_Prior = 100**100
purchase_Sum = productunov1000_Sum =  0
while proceed_Ask.upper().strip() in 'YES':
    name_Ask = str(input('Product name: '))
    price_Ask = float(input('Price:     R$ '))
    purchase_Sum = purchase_Sum + price_Ask
    if price_Ask > 1000: productunov1000_Sum =+ 1
    if price_Ask < price_Prior and price_Ask < cheapest_Wrt:
        cheapest_Nam = name_Ask.lower().strip()
        cheapest_Wrt = price_Ask
    price_Prior = price_Ask
    proceed_Ask = str(input('Proceed [Y/N]? '))
print(f'The total of purchase is R${purchase_Sum:.2f}\nHas {productunov1000_Sum} product over R$1000.00\nThe cheapest product is {cheapest_Nam} that worth R${cheapest_Wrt:.2f}')
