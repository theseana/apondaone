# for variable_name in range():
# '    '  <<< we call this space indent

for i in range(7):
  print('Man Amadeh Am.')
  print('Vay Vay!')
print('********************')

# range(n)  ->> 0, ..., n-1
# range(7)  ->>  0, 1, 2, 3, 4 ,5, 6

for i in range(7):
  print(i, type(i))
print('********************')

# range(n, m)   ->>  n, ..., m-1
# range(7, 13)  ->>  7, 8, 9, 10, 11 ,12
for i in range(7, 13):
  print(i, type(i))
print('********************')

# range(n, m, s)   ->>  n, n+s, n+2s, ..., m-1
# range(7, 14, 2)  ->>  7, 9, 11, 13
for i in range(7, 14, 2):
  print(i, type(i))
