import turtle
import random 

turtle.speed(1000)

for j in range(100):
    turtle.penup()
    x = random.randint(-600, 600)
    y = random.randint(-300, 300)
    turtle.goto(x, y)
    turtle.pendown()

    size = random.randint(10, 300)
    turtle.pensize(random.randint(1, 5))

    turtle.begin_fill()
    for i in range(4):
        turtle.fd(size)
        turtle.lt(90)
    turtle.end_fill()

turtle.done()
