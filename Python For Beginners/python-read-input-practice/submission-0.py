def add_two_numbers() -> int:
    line = input()
    new_input = line.split(",")

    num1 = int(new_input[0])
    num2 = int(new_input[1])

    return num1 + num2


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
