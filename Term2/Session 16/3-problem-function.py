def get_inputs():
    first_input = input("Enter your number: ")
    numbers_list = []
    while(first_input):
        numbers_list.append(int(first_input))
        first_input = input("Enter your number: ")
    return numbers_list

def sum_inputs(numbers_list):
    temp = 0
    for number in numbers_list:
        temp += number
    return temp

def avrage_calculator(numbers_list):
    count = len(numbers_list)
    total = sum_inputs(numbers_list)
    avrage = total / count
    print(f"Sum of my numbers: {total}")
    print(f"Avrage of my numbers: {avrage}")
    print(f"My numbers: {numbers_list}")

inputs = get_inputs()
avrage_calculator(inputs)
