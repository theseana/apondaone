odd = []
even = []

number = input("Enter your number: ")

while number:
    number = int(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
        
    number = input("Enter your number: ")
print(f"Odd{odd}\nEven{even}")