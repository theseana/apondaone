from os import linesep


file = open('athlete.txt', 'r')

lines = file.readlines()
print(lines)
file.close()
