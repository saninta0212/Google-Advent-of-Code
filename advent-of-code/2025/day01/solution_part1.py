from utils.helpers import read_input

path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day01/input.txt"
iterator = read_input(path)
start = 50
n_0 = 0

def move_dial(direction, steps, start):
    steps = steps%100
    if direction == "L":
        new_position = (start - steps)%100
    if direction == "R":
        new_position = (start + steps)%100
    return new_position
    
    
for line in iterator:
    operation = str(line.strip())
    direction = operation[0]
    steps = int(operation[1:])
    next_step = move_dial(direction, steps, start)
    if next_step == 0:
        n_0 += 1
    start = next_step
    print(next_step)

print(f"Result: {n_0}")
iterator.close()


    