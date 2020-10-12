# lower, upper, title, capitalize, isupper, islower
# istitle, swapcase
g = "HI"

"HI".lower() # firsth method
g.lower()    # second method

print(g.lower())
print(g)

g = g.lower()
print(g)
# ######################################################## #
g = "Python"
print(g.lower())  # "Python" >> "python"
print(g.upper())  # "Python" >> "PYTHON"

txt = "Welcome to my world"
print(g.title())        # "welcome to my world" >> "Welcome To My World"
print(g.capitalize())   # "welcome to my world" >> "Welcome to my world"

g = "python"
print(g.islower())      # "h" >>> True
g = "pythoN"
print(g.islower())      # "H" >>> False

# isupper check for Upper Case !
# "H" >>> True
# "h" >>> False

# istitle
# "Hello World!" >>> True
# "Hello world!" >>> False

g = "pYTHON"
print(g)            # "pYTHON"
print(g.swapcase()) # "Python"