chocolateBar = 1.50

print(f'Chocolate bars are ${chocolateBar:.2f}, how many do you want fatty?')
number = int(input())

if number >= 20:
    print(f'The price for {number} bars is ${((chocolateBar * 0.9) * number):.2f}')
else:
    print(f'The price for {number} bars is ${(chocolateBar * number):.2f}')