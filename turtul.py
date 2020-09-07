import turtle

x = turtle.Turtle()
x.color('#123210', 'blue')

x.begin_fill()
x.forward(100)
x.left(90)
x.forward(100)
x.left(90)
x.forward(100)
x.left(90)
x.forward(100)
x.end_fill()

x.penup()
x.forward(100)
x.pendown()

x.begin_fill()
x.forward(100)
x.left(90)
x.forward(100)
x.left(90)
x.forward(100)
x.left(90)
x.forward(100)
x.end_fill()

turtle.done()