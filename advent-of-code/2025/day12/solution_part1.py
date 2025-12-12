path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day12/input.txt"

with open(path) as f:
    blocks = f.read().strip().split("\n\n")

def calc_area(present_str):
    """Calculate area by counting # symbols"""
    area = 0
    for line in present_str.splitlines():
        area += line.count("#")
    return area

# Separate present definitions from region assignments
present_blocks = []
region_lines = []

for b in blocks:
    lines = b.splitlines()
    # If first line looks like "NxN: id id id", it's a region assignment
    if lines and 'x' in lines[0] and ':' in lines[0]:
        region_lines.extend(lines)
    else:
        # Otherwise it's a present definition
        present_blocks.append(b)

# Parse present definitions
gift = {}
for pb in present_blocks:
    lines = pb.split("\n", 1)  # Split on first newline only
    idx = int(lines[0].rstrip(':'))  # Remove the colon
    grid = lines[1] if len(lines) > 1 else ""
    gift[idx] = calc_area(grid)

print("Present areas:", gift)

# Check which regions can fit their assigned presents
fit_count = 0

for line in region_lines:
    size, number_ids = line.split(":")
    w, h = map(int, size.split("x"))
    total_region_area = w * h
    
    present_counts = list(map(int, number_ids.strip().split()))

    total_present_area = 0
    for index_gift in range(len(present_counts)):
        total_present_area += gift[index_gift] * present_counts[index_gift]
    

    fits = total_present_area <= total_region_area
    print(f"{size}: presents {present_counts}, need {total_present_area}, have {total_region_area}, fits: {fits}")
    
    if fits:
        fit_count += 1

print(f"\nRegions that can fit all assigned presents: {fit_count}")