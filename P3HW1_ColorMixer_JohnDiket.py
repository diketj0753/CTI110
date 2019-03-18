# This program will tell you a secondary color result from mixing two
# primary colors.
#
# CTI-110 
# P3HW1 - Color Mixer 
# John Diket
# February 11, 2019
#

# Let the user know what the program does.
print('Let\'s make a secondary color!')

# Take input of two chosen colors.
Color1=input('Choose a color: Red, Blue, or Yellow? ')

Color2=input('Choose a second color: Red, Blue, or Yellow? ')

# Mix the colors.
if Color1.lower() == 'red':
    if Color2.lower() == 'blue':
        print('When you mix Red and Blue, you get Purple!')
    elif Color2.lower() == 'yellow':
        print('When you mix Red and Yellow, you get Orange!')
    else:
        print('You need to choose either Blue or Yellow.')
elif Color1.lower() == 'blue':
    if Color2.lower() == 'red':
        print('When you mix Red and Blue, you get Purple!')
    elif Color2.lower() == 'yellow':
        print('When you mix Blue and Yellow, you get Green!')
    else:
            print('You need to choose either Red or Yellow.')
elif Color1.lower() == 'yellow':
    if Color2.lower() == 'blue':
        print('When you mix Yellow and Blue, you get Green!')
    elif Color2.lower() == 'red':
        print('When you mix Red and Yellow, you get Orange!')
    else:
        print('You need to choose either Blue or Yellow.')
else:
    print('You need to choose one of the primary colors \
Red, Blue, or Yellow.')

input()
