# This is comment in the Debug Lab.
#
# CTI 110 P3Lab_Debug
# Diket, John
# February 20, 2019

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    # Define the program for the user.
    print('This program will tell you the letter grade for you score.')

    # Get the grade score from the user.
    score = int(input('\nEnter grade: '))
    
    # Determine grade and output
    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')

    input()

# program start
main()
