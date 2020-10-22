things = ["ball", "tshirt", "axe"]
material = ["woody", "metalic", "plastic"]
colors = ["yellow", "green", "brown"]

for color, material, thing in zip(colors, material, things): 
    print(color, material, thing)
