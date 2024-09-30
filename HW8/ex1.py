import random

with open('random_numbers.txt', 'w') as file:
    for _ in range(1000):
        number = random.randint(0, 100)
        file.write(f"{number}\n")

