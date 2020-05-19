
from random import randint

def start():
    user_numbers = get_lottery_numbers()
    randomized_numbers = randomize_lottery_numbers()

    print(f"\nUser numbers {user_numbers}")
    print(f"\nRandomized numbers {randomized_numbers}")

    result = set.intersection(user_numbers, randomized_numbers)
    print(f"\nYou got {result} numbers right, price of winning is {100 * len(result)}£.")

def get_lottery_numbers():
    numbers = input("\nEnter 6 numbers, separated by comma: ")
    splitted_numbers = numbers.split(",")
    int_set = {int(number) for number in splitted_numbers}
    return int_set

def randomize_lottery_numbers():
    # Set will be initialized using set() not {}
    numbers = set()
    while len(numbers) < 6:
        numbers.add(randint(1, 20))
    return numbers

start()
