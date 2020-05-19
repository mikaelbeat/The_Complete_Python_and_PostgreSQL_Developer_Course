
numbers = "1,2,3,4,5,6"
split_numbers = numbers.split(",")
# numbers_as_int = []

# for number in split_numbers:
#     numbers_as_int.append(int(number))

# print(numbers_as_int)

# List comprehension solution for converting list of string numbers to int
print([int(number) for number in split_numbers])
