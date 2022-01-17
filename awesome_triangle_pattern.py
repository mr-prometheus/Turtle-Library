import turtle
win = turtle.Screen()
dist = 1
flag = 500
win.bgcolor("black")
alex = turtle.Turtle()
alex.speed(1000)
alex.color("cyan")
while flag:
    alex.forward(dist)
    alex.left(120)
    alex.left(1)
    dist +=1
    flag -=1

turtle.done()
win.exitonclick()