# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$ Type Casting - DataType COnversion $$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# First Method
print('Salary Calculator!')
hour = input('Hour in Week: ')
hour = int(hour)
salary = input('Salary per Hour: ')
salary = int(salary)
print(hour * salary)

# Second Method
print('Salary Calculator!')
hour = int(input('Hour in Week: '))
salary = int(input('Salary per Hour: '))
print(hour * salary)

# Third Method
print('Salary Calculator!')
hour = input('Hour in Week: ')
salary = input('Salary per Hour: ')
print(int(hour) * int(salary))