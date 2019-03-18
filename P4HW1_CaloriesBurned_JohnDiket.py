# This program displays calories burned while running on a treadmill.
#
# February 25, 2019
# CTI-110 P4HW1 - Calories Burned
# John Diket

# Let the user know what the program does.
print('This program outputs calories burned when running on a treadmill.\n')

for time in [20, 35, 45]:
    print('After running for', time, 'minutes you will have burned' \
          , time*5,'calories.')

input()
