import json


# file = open('3-names.json', 'r')
# file_json = json.load(file)
# file.close()

with open('3-names.json', 'r') as file:
    file_json = json.load(file)

for i in file_json:
    if i["name"] == "romina":
        print(i["last"])

for i in file_json:
    if i["name"] == "arvin":
        i["last"] = "al'e seyed"

with open('3-names.json', 'w') as outfile:
    json.dump(file_json, outfile, indent=4)