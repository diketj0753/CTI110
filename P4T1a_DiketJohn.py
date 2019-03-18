# Tutorial with turtle drawing shapes.
#
# CTI-110 - P4T1 Turtle Graphics
# March 11, 2019
# John Diket


# Initialize turtle and set shape.
import turtle
wn = turtle.Screen()
wn.title('Shapes!')
turtle.shape('turtle')

# Draw the square.
turtle.color('blue')
for turns in range(1,5):
    turtle.forward(50)
    turtle.right(90)

# Draw the triangle.
turtle.color('red')
for turns in range(1,4):
    turtle.left(120)
    turtle.forward(50)

wn.exitonclick()
