def x(number):
    number = str(number)
    numbers = list(number)
    new_numbers = []
    for i in range(6):
        poped = numbers.pop()
        numbers.insert(0, poped)
        temp = ''.join(numbers)
        new_numbers.append(temp.lstrip('0'))
    print(new_numbers)




x(123406)