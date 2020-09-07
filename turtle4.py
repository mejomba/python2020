import turtle

x = turtle.Turtle()
x.speed(10)
x.penup()
x.goto((-300,0))
x.pendown()
x.color('red', 'blue')
x.getscreen().bgcolor('orange')


def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            turtle.begin_fill()
            turtle.forward(size)
            star(turtle, size / 3)
            turtle.left(216)
            turtle.end_fill()


star(x, 300)
turtle.done()