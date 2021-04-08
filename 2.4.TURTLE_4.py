import turtle
wn = turtle.Screen()

elan = turtle.Turtle()
elan.color('blue')
distance = 0.01
for _ in range(100):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10
wn.exitonclick()
