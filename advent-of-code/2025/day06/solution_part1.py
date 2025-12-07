from functools import reduce
import operator
path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day06/input.txt"

with open(path) as f:
    content = f.read().strip()

parts = content.split("\n")
split_lines = [line.split() for line in parts]
columns = len(parts[0].split())

total = 0

for col in range(columns):
    sequence = []
    for line in parts:
        sequence = [split_lines[row][col] for row in range(len(split_lines))]
    operation = sequence[-1]
    numbers = [int(x) for x in sequence[:-1]]
    
    if operation == "+":
        total += sum(numbers)
    else:
        total += reduce(operator.mul, numbers, 1)

print(total)