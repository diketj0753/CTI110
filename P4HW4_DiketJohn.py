# Nested loop for drawing pictures.
#
# March 11, 2019
# CTI-110 P4HW4 - Nested Loops
# John Diket


# Initialize and setup turtle.
import turtle
import random
wn=turtle.Screen()
wn.title('Nested Loops')
wn.bgcolor('black')

# Color list.
color=['red', 'blue', 'yellow', 'white', 'purple', 'green'] 

# First loop to begin pattern.
for outside in range(1,9):
    # change pen size using random integer between 5 and 25.
    turtle.pensize(random.randint(5, 25))
    turtle.forward(150)
    # internal look for end shape.
    for inside in range(1,9):
        # random color change using created list.
        turtle.color(random.choice(color))
        turtle.left(30)
        turtle.forward(10)

wn.exitonclick()
        
