bascket = [
    'apple',
    'apple',
    'kiwi',
    'kiwi',
    'kiwi',
    'banana',
]

counter = {}

for friut in bascket:
    if friut in counter:
        counter[friut] += 1
    else:
        counter[friut] = 1
print(counter)