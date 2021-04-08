import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.penup()#this thing is of no use, whether you write it or not
tess.color("blue")
tess.shape('turtle')

dist = 15                     # this is new
for _ in range(45):    # start with size = 5 and grow by 2
#45 is the total no. of turtles you would see in the picture
    tess.stamp()             # leave an impression on the canvas
#if you write stamp(), then run to understand, if not, again run to see what actually stamp is doing
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 1#1 is the length of gap incrementing after every loop(you can write any no.)
wn.exitonclick()
