import turtle
window = turtle.Screen()
alex = turtle.Turtle()
window.bgcolor("black")
alex.color("cyan")
alex.speed(1000)
k =0 
d=0
while True:
    for i in range(4):
        alex.forward(50)
        alex.left(90)
    alex.left(15)
    k += 1 
    if k >=360/15:

        alex.left(30)
        alex.forward(50)
        k=0
        d +=1
        if d>=12:
            break
    
window.exitonclick()
