file = open('2-.txt', 'r')
for line in file:
    if 'last' in line:
        print(line)