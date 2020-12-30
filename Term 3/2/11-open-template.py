# remove all data and add new data
file = open('athlete.txt', 'w')

template = """
Name: {}
Last: {}
Phone: {}
################
"""

file.write(template.format('John', 'Lenon', '0012212145415'))

file.close()