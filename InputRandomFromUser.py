import random

try:
    numbers = raw_input("How many numbers do you want generated? ")
    for num in range(int(random.random() + 1), int(numbers) + 1):
        print(random.randint(num, num * 10))
except ValueError:
    print("Input is invalid!")