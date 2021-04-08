import turtle
n=int(input('ENTER THE NO. OF SIDES OF THE POLYGON YOU WANT: '))
if n<3:
    print("YOU ARE A FOOL, THAT'S ALLLLL!")
else:
    a=int(input('ENTER THE LENGTH OF EACH SIDE YOU WANT(IN PIXELS): '))
    y=str(input('ENTER THE COLOR FOR BACKGROUND: '))
    e=str(input('ENTER THE COLOR FOR THE LINES: '))
    x=((n-2)*180)/n
    m=180-x
    board=turtle.Screen()
    board.bgcolor(y)
    line=turtle.Turtle()
    line.color(e)
    line.pensize(1)
    line.forward(a)
    for i in range(n):
        line.left(m)
        line.forward(a)
    board.exitonclick()
