# This program will receive an input from the user
# for pounds and output the value in kilograms.
#
# February 6, 2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# John Diket
#
# Explain the program to the user.
print('This program will convert pounds into kilograms.')
      
# Receive a starting value in pounds.
weight_lbs=float(input('\nPlease enter a weight in pounds: '))

# Convert lbs to kg by dividing weight_lbs input by 2.046.
weight_kg=float(weight_lbs/2.2046)

# Outputs the final value in kilograms with formatting to easily read
print('\nThat is %s kilograms.' % format(weight_kg, ',.2f'))


input()
