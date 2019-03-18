# Snowflake for extra credit.
#
# March 11, 2019
# CTI-110 P4T1 - Snowflake
# John Diket

# Initialize and setup turtle.
import turtle
wn=turtle.Screen()
wn.bgcolor('cyan')

# Loop for creating hexagon base shape and long arm of branch.
for hex in range(1,7):
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(50)
    turtle.backward(40)
    # Loop for creating branch at vertices.
    for i in range(1,3):
        turtle.left(45)
        turtle.forward(20)
        turtle.backward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.backward(20)
        turtle.left(45)
    # Return turtle to vertex position to continue.
    turtle.backward(10)
    turtle.right(120)

wn.exitonclick()
