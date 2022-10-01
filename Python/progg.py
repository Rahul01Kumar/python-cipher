import turtle
rahul=turtle.Turtle()
rahul.speed(0)
rahul.color('red')

for i in range(180):
    rahul.forward(100)
    rahul.right(30)
    rahul.forward(20)
    rahul.left(60)
    rahul.forward(50)
    rahul.right(30)

    rahul.penup()
    rahul.setposition(0,0)
    rahul.pendown()
    rahul.right(2)

turtle.done()
