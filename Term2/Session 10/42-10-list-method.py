basket = ["Kiwi", "Apple"]
basket.append("Watermelon")
print(basket)
print(basket.count("A"))    

# basket.append("Watermelon","Sugar")
# it raises error

# ???
a = ["1", "B", "C", "D", "E", ["1", "2"]]
print(a[5])
print(a[5][1])

basket.append(["Watermelon","Sugar"])
print(basket)

print("***********************")

q = ["q", "w","e"]
r = ["r", "t"]

print(q.extend(r))
print(q)
print(r)

print(q.index("q"))

q.insert(3, "Z")
print(q)

poped_element = q.pop()
print(q)
print(poped_element)

poped_zero_index = q.pop(0)
print(q)
print(poped_zero_index)

q.remove("Z")
print(q)

q.sort(reverse=False)
print(q)