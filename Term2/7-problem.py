# Enter radius of your Circle: 1
# Perimeter of your Circle is: 6.28 
# Area of your Circle is: 3.14
# power **

# Perimeter: 2 x pi x r
# Area: pi x r^2

import math

radius = float(input('Enter radius of your Circle: '))
pi = 3.14

p = 2 * pi * radius
print('Perimeter of your Circle is:', p)

a = pi * radius**2
print('Area of your Circle is:', a)