import turtle
import random 


turtle.penup()
x = random.randint(-600, 600)
y = random.randint(-300, 300)
turtle.goto(x, y)
turtle.pendown()
turtle.fd(300)

turtle.done()
