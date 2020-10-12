# a = '42'
# print(type(a))
# a = int(a)
# print(type(a))

# b = 'a2'
# print(type(b))
# b = int(b)  ERROR ->>>> this cause error!!! because of 'a' in 'a2'

# c = 3.141592
# print(type(c))
# c = int(c)
# print(c, type(c))

d = '3.141592'
print(type(d))
d = int(float(d))
print(d, type(d))
