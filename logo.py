import turtle
import time

# t = time.time()
s = turtle.Screen()
s.screensize(1920, 1080)
# s.bgcolor('#abc')
x = turtle.Turtle()
# time.sleep(3)
x.speed(10)
x.pensize(2)
x.color( '#7a28a3')
time.sleep(3)

x.penup()
x.goto(-900, 450)
x.pendown()
x.forward(1800)
x.right(90)
x.forward(900)
x.right(90)
x.forward(1800)
x.right(90)
x.forward(900)
x.right(90)
x.penup()
x.goto(0,0)
x.pendown()

x.speed(6)

x.left(130)
x.forward(200)
x.right(90)
x.forward(40)
x.right(90)
x.forward(200)

x.left(90)
x.forward(200)
x.right(90)
x.forward(40)
x.right(90)
x.forward(200)

x.forward(400)
x.right(90)
x.forward(40)
x.right(90)
x.forward(360)

x.penup()
x.forward(240)
x.right(90)
x.forward(40)
x.pendown()


x.speed(100)
x.pensize(3)
# x.color('#7a28a3')
x.color('red')

for i in range(1,38):
    x.forward(13)
    x.right(5)
    x.pensize(i)
    # x.pensize(a[i])

x.color('#7a28a3') # color for y
x.penup()
x.forward(45)
x.pendown()

x.color('blue')
a = list(range(40))
a.reverse()
for j in range(1, 40):
    x.forward(13.5)
    x.left(5)
    # x.pensize(j)
    x.pensize(a[j])
x.forward(1)
x.color('#000')
#

# x.speed(2)
#
x.hideturtle()
x.penup()
x.goto(190, -380)
x.pendown()

# x.color('#FF8C00')
x.color('purple')
x.pensize(0)
# x.color('blue')
x.write("Pyproject", True, align="right", font=('arial black', 45, 'bold'))
#


turtle.done()
# print(time.time() - t)
