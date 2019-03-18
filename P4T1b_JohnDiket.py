# Using turtle to draw initials.
#
#March 11, 2019
# CTI-110 P4T1b-Initials
# John Diket

# Initialize and setup turtle.
import turtle
turtle.shape('turtle')
wn=turtle.Screen()
wn.title('JD')
turtle.pencolor('red')
turtle.pensize(5)



# Draw J
turtle.right(90)
turtle.forward(150)
for turns in range(1,35):
    turtle.right(5)
    turtle.forward(5)

# reset turtle location
turtle.penup()
turtle.home()

# Draw D
turtle.forward(50)
turtle.pendown()
for turns in range(1,60):
    turtle.right(3)
    turtle.forward(5)
turtle.right(93)
turtle.forward(185)

wn.exitonclick()
