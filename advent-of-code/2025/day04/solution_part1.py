from utils.helpers import read_input

path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day04/input.txt"
grid = [list(row.strip()) for row in read_input(path)]

rows = len(grid)
cols = len(grid[0])
accessible = 0

# 8 directions around a cell
DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),         ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def isValid(r, c):
    # Only care about cells that are '@'
    if grid[r][c] != '@':
        return False
    
    neighbor_count = 0
    
    for dr, dc in DIRS:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                neighbor_count += 1
    
    return neighbor_count < 4


# Count all accessible '@'
for r in range(rows):
    for c in range(cols):
        if isValid(r, c):
            accessible += 1

print("Accessible rolls:", accessible)
