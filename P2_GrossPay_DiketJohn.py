# This program takes hours worked and hourly pay rate to produce gross pay.
# 
# Creates a variable named Hours by requesting information from user.
Hours=float(input('How many hours did you work last week? '))

# Creates a variable named PRate with user generated information.
PRate=float(input('What is your hourly pay rate? '))

# Multiplies the two variables together to determine Gross Pay and rounds to
# two decimal places.
GrossPay=float(Hours*PRate)

# Outputs the Gross Pay for the user
print('Your Gross Pay for the previous week will be $',
      format(GrossPay,',.2f'), sep='')

input()
