import random

numbers = [random.randint(1, 10000) for _ in range(250)]
numbers.reverse()

print(f'Reverse list: {numbers}')