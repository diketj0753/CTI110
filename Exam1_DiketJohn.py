# Program for Exam 1 in Python Module 3
#
# John Diket
# February 18, 2019

# Welcome statement.
print('Welcome! This program will determine if a number \
is positive or negative.')

# Requesting number input from user.
number=int(input('Please enter a whole number: '))


# Evaluating number and outputing result.
if number > 0:
    print(number, 'is a positive number.')
elif number < 0:
    print(number, 'is a negative number.')
else:
    print('You entered zero.')

input()
