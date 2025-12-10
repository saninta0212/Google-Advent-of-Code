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

visited = set()

def count(a, beam):
    # Base case: check bounds
    if a >= len(smokes) or beam < 0 or beam >= len(smokes[a]):
        return 0
    
    # Check if already visited this position
    if (a, beam) in visited:
        return 0
    
    visited.add((a, beam))
    
    if smokes[a][beam] == "^":
        # This is a split! Count it and continue with both beams
        return 1 + count(a+1, beam+1) + count(a+1, beam-1)
    
    elif smokes[a][beam] == ".":
        # Just continue straight down
        return count(a+1, beam)

    return 0

total_count = count(0, beam)
print(total_count)