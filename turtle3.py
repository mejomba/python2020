import turtle
import math

x = turtle.Turtle()

x.speed(1000)
x.color('blue')

for i in range(700):
    x.forward(10)
    x.left(math.sin(i/10)*25)
    x.left(25)

turtle.done()