import turtle as tr
from turtle import pencolor


def square(size, pen_size, pen_color):
    tr.pencolor(pen_color)
    tr.pensize(pen_size)
    for loop in range(4):
        tr.fd(size)
        tr.lt(90)


pen_color = tr.textinput('Pen Color', 'Enter Color of Pen: ')
pen_size = tr.numinput('Pen Size', 'Enter size of Pen: ')
square_size = tr.numinput('Square Size', 'Enter size of Square: ')
square(square_size, pen_size, pen_color)
tr.done()
