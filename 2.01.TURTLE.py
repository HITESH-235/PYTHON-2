import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.forward(75+75)         # tell alex to move forward by 150 units
alex.left(72)             # turn by 90 degrees
alex.forward(150)          # complete the second side of a rectangle
alex.left(72)
alex.forward(150)
alex.left(72)
alex.forward(150)
alex.left(72)
alex.forward(150)
wn.exitonclick()
