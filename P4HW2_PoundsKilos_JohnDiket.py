# This program displays a conversion table for pounds and kilograms
#
# February 25, 2019
# CTI-110 P4HW2 - Pounds to Kilos Table
# John Diket


# Print the table headings.
print('Pounds\tKilos')
print('-------------')

# Print out the values for lbs and kg from 100 to 300
# pounds in steps of 10.
for pounds in range(100, 310, 10):
    kilos=pounds/2.2046
    print(pounds, '\t', format(kilos, '.1f'))

input()
