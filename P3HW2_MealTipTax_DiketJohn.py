# This program will take a sub-total bill amount, ask the user what they
# want to tip, and give them a new total that inclus tax and tip.
#
# CTI-110
# P3HW2 - MealTipTax 
# John Diket
# February 18, 2019
#
print('This program can be used to easily calculate tip and tax for a food bill.',
      '\nIt will output 15%, 18%, or 20% tip amounts and your new total.')

# Request inital bill amount.
SubTotal=float(input('\nHow much is the bill before including tip? '))
TipA=int(input('Would you like to leave a 15%, 18%, or 20% tip? '))

# Calculate 7% tax.
Tax=SubTotal*0.07

# Decision structure and operations for output.
if TipA==15:
    TipV=SubTotal*0.15
    Total=SubTotal+Tax+TipV
    print('\nFor a 15% tip, the tip is: $', format(TipV, ',.2f'),'. \
  \nThe tax wil be: $', format(Tax, ',.2f'),'. \
  \nMaking the total bill: $', format(Total, ',.2f'), sep='')
elif TipA==18:
    TipV=SubTotal*0.18
    Total=SubTotal+Tax+TipV
    print('\nFor an 18% tip, the tip is: $', format(TipV, ',.2f'),'. \
  \nThe tax wil be: $', format(Tax, ',.2f'),'. \
  \nMaking the total bill: $', format(Total, ',.2f'), sep='')
elif TipA==20:
    TipV=SubTotal*0.2
    Total=SubTotal+Tax+TipV
    print('\nFor a 20% tip, the tip is: $', format(TipV, ',.2f'),'. \
  \nThe tax wil be: $', format(Tax, ',.2f'),'. \
  \nMaking the total bill: $', format(Total, ',.2f'), sep='')
else:
    print('You need to choose tip amounts of 15%, 18%, or 20%.')

input()
