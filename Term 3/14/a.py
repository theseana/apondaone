import json

with open('a.json', 'r') as j_file:
    a = json.load(j_file)
    b = {"name": "koroush"}
    a.append(b)

with open('a.json', 'w') as file:
    json.dump(a,file, indent=4)
