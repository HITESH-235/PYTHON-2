import turtle
n=int(input('ENTER THE NO. OF SIDES OF THE POLYGON YOU WANT: '))
if n<3:
    print("YOU ARE A FOOL, THAT'S ALLLLL!")
else:
    a=int(input('ENTER THE LENGTH OF EACH SIDE YOU WANT(IN PIXELS): '))
    x=((n-2)*180)/n
    m=180-x
    board=turtle.Screen()
    line=turtle.Turtle()
    line.forward(a)
    for i in range(n):
        line.left(m)
        line.forward(a)
