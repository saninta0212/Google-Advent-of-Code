from functools import reduce
import operator

path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day06/input.txt"

with open(path) as f:
    content = f.read().strip()

lines = content.split("\n")

# Pad all lines to same length
max_len = max(len(line) for line in lines)
padded = [line.ljust(max_len) for line in lines]

operators_line = padded[-1]
num_lines = padded[:-1]

total = 0
current_numbers = []
current_op = None

# Process character positions RIGHT-TO-LEFT
for col_idx in range(max_len - 1, -1, -1):
    op_char = operators_line[col_idx]
    
    # Collect digits from this column (top-to-bottom)
    digits = ''.join(line[col_idx] for line in num_lines if line[col_idx].isdigit())
    
    if digits:
        current_numbers.append(int(digits))
    
    # When we hit an operator (non-space), process accumulated numbers
    if op_char in '+*':
        if current_numbers:
            if op_char == '+':
                total += sum(current_numbers)
            else:
                total += reduce(operator.mul, current_numbers, 1)
            current_numbers = []

print(total)