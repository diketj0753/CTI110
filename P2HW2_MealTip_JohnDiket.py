# This program will take a pre-tip value for a bill and give totals
# for 15%, 18%, and 20% tip amounts and the total bill.
# 
# February 6, 2019
# CTI-110 P2HW2 - Meal Tip Calculator
# John Diket
#
# Explain the program to the user.
print('This program can be used to easily calculate tip for a food bill.',
      '\nIt will output 15%, 18%, and 20% tip amounts and your new total.')

# Request inital bill amount.
PreTip=float(input('\nHow much is the bill before including tip? '))

# Calculate the various tip amounts and totals.
Tip15=PreTip*.15
Total15=PreTip+Tip15

Tip18=PreTip*.18
Total18=PreTip+Tip18

Tip20=PreTip*.2
Total20=PreTip+Tip20

# Display the tip amounts and total bill value.
print('\nFor a 15% tip, the tip is $', format(Tip15, ',.2f'),'. \
  Making the total bill $', format(Total15, ',.2f'), sep='')

print('\nFor a 18% tip, the tip is $', format(Tip18, ',.2f'),'. \
  Making the total bill $', format(Total18, ',.2f'), sep='')

print('\nFor a 20% tip, the tip is $', format(Tip20, ',.2f'),'. \
  Making the total bill $', format(Total20, ',.2f'), sep='')

input()
