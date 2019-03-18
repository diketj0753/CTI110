# This program will evaluate the area of two different rectangles for
# which has the greatest area.
#
# CTI-110-AreaOfRectangles
# John Diket
# February 18, 2019

# Introduction statement.
print('This program will ask you for length and width of two rectangles, \
then compare the area to see which is greater.')

# Obtaining the values from the user.
Length1=float(input('Please enter the length of the first rectangle: '))
Width1=float(input('Please enter the width of the first rectangle: '))
Length2=float(input('Please enter the length of the second rectangle: '))
Width2=float(input('Please enter the width of the second rectangle: '))

# Computing the area of both rectangles.
Area1=Length1*Width1
Area2=Length2*Width2

# Determining results and outputing for user.
if Area1 > Area2:
    print('The first rectangle has the larger area of', format(Area1, ',.2f'))
elif Area2 > Area1:
    print('The second rectangle has the larger area of', format(Area2, ',.2f'))
else:
    print('The rectangles have an equal area of', format(Area1, ',.2f'))

input()
