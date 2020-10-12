import turtle
import random 

turtle.speed(1000)

turtle.color('red')

turtle.begin_fill()
for i in range(4):
    turtle.fd(100)
    turtle.lt(90)
turtle.end_fill()

turtle.done()
