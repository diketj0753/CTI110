Hours=float(input('How many hours did you work last week? '))

# Creates a variable named PRate with user generated information.
GrossPay=float(input('How much did you make over this time? '))

# Multiplies the two variables together to determine Gross Pay and rounds to
# two decimal places.
PRate=float(GrossPay/Hours)

# Outputs the Gross Pay for the user
print('Your Hourly Rate for the previous week was $',
      format(PRate,',.2f'), sep='')

input()
