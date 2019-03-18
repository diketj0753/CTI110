# This program evaluates sales commissions.

# Variable to control the loop.
keep_going = 'y'

# Calculations for commission.
while keep_going == 'y':
    sales=float(input('Enter the total amount of sales: '))
    comm_rate=float(input('What is the commission rate? '))
    comm_perc=comm_rate/100
    commission=sales*comm_perc
    print('The commission is $', format(commission, ',.2f'), sep='')
    keep_going=input('Would you like to calculate another commission? y or n: ')
