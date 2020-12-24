def get_detail(string):
    temp = string.split()
    return temp[0], temp[1]


name, family = get_detail('sina bakhshandeh')
print(name)
print(family)