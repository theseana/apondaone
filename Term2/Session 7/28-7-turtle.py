import turtle as tr

size = int(input('Enter size of Square: '))
angle = int(input('Angle in each turn: '))
number = int(360 / angle)

tr.speed(1000)
tr.color('red')
tr.pensize(3)

for j in range(number):
  for i in range(4):
    tr.fd(size)
    tr.lt(90)

  tr.left(angle)


tr.done()
