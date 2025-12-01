from utils.helpers import read_input
import math
path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day01/test.txt"
iterator = read_input(path)
start = 50
n_0 = 0
initial = 0

def move_dial(direction, steps, start):
    went_through_zero = 0
    went_through_zero_steps = steps//100
    steps = steps%100
    if direction == "L":
        move = (start - steps)
        went_through_zero = abs(move//100) # when move ends at 0, this gives an extra 1
        if move == 100:
            went_through_zero -= 1 if went_through_zero != 0 else 0
        new_position = move%100
    if direction == "R":
        move = (start + steps)
        went_through_zero = abs(move//100)  # when move ends at 0, this gives an extra 1
        if move == 100:
            went_through_zero -= 1 if went_through_zero != 0 else 0
        new_position = move%100
    if start == 0:
        went_through_zero -= 1 if went_through_zero != 0 else 0## When you start at zero and move the dial left, you result in neg number but you were at zero itwont count
    total_zero = went_through_zero+went_through_zero_steps
    print(f"went_through_zero: {went_through_zero}")
    print(f"went_through_zero_steps: {went_through_zero_steps}")
    return new_position, total_zero
    
    
for line in iterator:
    operation = str(line.strip())
    direction = operation[0]
    steps = int(operation[1:])
    next_step, went_through_zero = move_dial(direction, steps, start)
    if next_step == 0:
        n_0 += 1
    start = next_step
    initial = went_through_zero + initial
    print(f"Next step: {next_step}")
    print(f"Result ended at zero: {int(next_step==0)}")
    print(f"Result points at zero: {went_through_zero}")
    print("----------------------------------------------------")

print(f"Result pointed at zero: {n_0}")
print(f"Result went through zero: {initial}")
print(f"Total number of zeros: {n_0+initial}")
iterator.close()


    