from utils.helpers import read_input

path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day01/test.txt"
iterator = read_input(path)
start = 50
n_0 = 0
initial = 0

def move_dial(direction, steps, start):
    went_through_zero = 0
    steps = steps%100
    went_through_zero = steps//100
    if direction == "L":
        move = (start - steps)
        new_position = move%100
        went_through_zero = abs(move//100)
    if direction == "R":
        move = (start + steps)
        new_position = move%100
        went_through_zero = abs(move//100)
    return new_position, went_through_zero
    
    
for line in iterator:
    operation = str(line.strip())
    direction = operation[0]
    steps = int(operation[1:])
    next_step, went_through_zero = move_dial(direction, steps, start)
    if next_step == 0:
        n_0 += 1
    start = next_step
    initial = went_through_zero + initial
    print(next_step)

print(f"Result: {n_0}")
print(f"Result: {initial}")
print(f"Total number of zeros: {n_0+initial}")
iterator.close()


    