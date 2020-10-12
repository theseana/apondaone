all_money = float(input('All Money I Have: '))
price_iceCream = float(input('Price of one Ice Cream: '))
number = int(all_money / price_iceCream)
print('I have', all_money, '$ so I can buy', number,'Ice Cream for', number * price_iceCream,'$.')