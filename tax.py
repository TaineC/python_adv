country = input('What country do you live in? ')
earnings = input('What is your yearly salary?: ')
earnings = float(earnings)

if earnings <= 14000:
    tax = 1.105
elif earnings > 14000 or earnings <= 48000:
    tax = 1.175
elif earnings > 48000 or earnings <= 70000:
    tax = 1.3
else:
    tax = 1.33

total = (earnings / tax)

if country != 'New Zealand':
    print('Your tax can not be calculated under NZD')
else:
    print('Your income after tax is $' + str(round(total, 2)))

if country == 'New Zealand' and total >= 80000:
    print('You are in New Zealands higher income bracket')