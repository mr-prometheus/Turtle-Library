import turtle
win=turtle.Screen()
win.bgcolor("Black")
alex = turtle.Turtle()
alex.speed(1000)
alex.color("cyan")
forw = 1
while True:
    for i in range(3):
        alex.forward(forw)
        alex.left(120)
    forw += 1
    alex.penup()
    alex.left(5)
    alex.forward(2)
    alex.left(5)
    alex.pendown()

turtle.done()