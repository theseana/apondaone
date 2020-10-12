name = 'Sina'
last = 'Bakhshandeh'
age = 29
nationality = 'Iran'

a = 'I am Sina Bakhshandeh 29 years old, from iran.'
# print(a)

# print('I am', name, last, age ,'years old, from ', nationality)

b = 'I am {} {} {} years old, from {}.'

print( b.format(name, last, age, nationality) )