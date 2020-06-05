
def add(value1, value2):
    return value1 + value2

# Passing as arguments
nums = [3, 5]
print(add(*nums))
print("\n")

# Passing as keyword arguments
nums2 = {"value1": 10, "value2": 15}
print(add(**nums2))
print("\n")


def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

def calculator(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided!"

print(calculator(5, 2, operator="*"))

