path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day07/input.txt"

with open(path) as f:
    content = f.read().split("\n")
    
characters = content[0]
beam = 0

for i in range(0, len(characters)):
    if characters[i] == "S":
        beam = i
        break
    
smokes = [list(line) for line in content[1:]]

from functools import lru_cache

@lru_cache(maxsize=None)
def count_timelines(row, col):
    if row >= len(smokes) or col < 0 or col >= len(smokes[row]):
        return 1
    
    cell = smokes[row][col]
    
    if cell == "^":
        return count_timelines(row + 1, col - 1) + count_timelines(row + 1, col + 1)
    elif cell == ".":
        return count_timelines(row + 1, col)
    
    return 0

total_timelines = count_timelines(0, beam)
print(total_timelines)