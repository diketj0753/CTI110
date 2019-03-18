# Program calculates the sum of numbers given by the user.
#
# February 25, 2019
# CTI-110 P4HW3 - Sum of Numbers
# John Diket

# Welcome the user.
print('This program will add up all the numbers you enter.\n\
When you are done entering numbers, type in 0 (zero) to see the total.')

# Start the accumulator variable.
total=0.0

# Get first number.
num=float(input('Please enter a positive number, or 0 to end: '))

# Collect the numbers and keep the total.
while num != 0:
    num=float(input('Please enter a positive number, or 0 to end: '))
    total=total+num

# Output the total.
print('The total is: ', format(total, ',.3f'))

input()
