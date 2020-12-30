file = open('athlete.txt', 'r')

line = file.readline()
while line != '':
    if 'First' in line:
        line = line.split('  ')
        print(line[1])
    if 'Last' in line:
        line = line.split('   ')
        print(line[1])
    line = file.readline()

file.close()
